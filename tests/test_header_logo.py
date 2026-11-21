"""
Testes do cabeçalho: logo e nome do projeto lado a lado (issue #13).
"""
import os
import tempfile
import unittest

from sphinx.application import Sphinx

import moodle_docs_theme

SVG = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 8 8"><rect width="8" height="8"/></svg>'


def build_header(extra_conf: str) -> str:
    """Compila um projeto mínimo e devolve o trecho do cabeçalho do index.html."""
    with tempfile.TemporaryDirectory() as tmp:
        src = os.path.join(tmp, "src")
        os.makedirs(src)
        with open(os.path.join(src, "logo.svg"), "w", encoding="utf-8") as f:
            f.write(SVG)
        with open(os.path.join(src, "index.rst"), "w", encoding="utf-8") as f:
            f.write("Teste\n=====\n")
        with open(os.path.join(src, "conf.py"), "w", encoding="utf-8") as f:
            f.write(
                'project = "Projeto Teste"\n'
                'extensions = ["moodle_docs_theme"]\n'
                'html_theme = "moodle_docs_theme"\n'
                f"html_theme_path = [{moodle_docs_theme.get_html_theme_path()!r}]\n"
                + extra_conf
            )
        out = os.path.join(tmp, "out")
        app = Sphinx(src, src, out, os.path.join(tmp, "doctrees"), "html",
                     status=None, warning=None, freshenv=True)
        app.build()
        with open(os.path.join(out, "index.html"), encoding="utf-8") as f:
            html = f.read()
    start = html.index('class="moodle-brand"')
    return html[start:html.index("</a>", start)]


class TestHeaderLogo(unittest.TestCase):

    def test_logo_and_title_side_by_side(self):
        header = build_header('html_logo = "logo.svg"\n')
        self.assertIn('class="moodle-brand-logo"', header)
        self.assertIn('class="moodle-brand-title"', header)
        self.assertIn("Projeto Teste", header)

    def test_title_without_logo(self):
        header = build_header("")
        self.assertNotIn('class="moodle-brand-logo"', header)
        self.assertIn('class="moodle-brand-title"', header)

    def test_logo_only_hides_visible_title(self):
        header = build_header('html_logo = "logo.svg"\nhtml_theme_options = {"logo_only": True}\n')
        self.assertIn('class="moodle-brand-logo"', header)
        self.assertNotIn('class="moodle-brand-title"', header)
        self.assertIn('class="visually-hidden"', header)


class TestHeaderCss(unittest.TestCase):

    def test_brand_group_is_vertically_centered(self):
        css_path = os.path.join(moodle_docs_theme.get_html_theme_path(), "static", "css", "base.css")
        with open(css_path, encoding="utf-8") as f:
            css = f.read()
        block = css[css.index(".moodle-brand-group {"):]
        block = block[:block.index("}")]
        self.assertIn("align-items: center", block)


if __name__ == "__main__":
    unittest.main()
