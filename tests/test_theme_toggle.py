"""
Testes do botão de tema: o rótulo nomeia a ação que executa (issue #15).
"""
import os
import tempfile
import unittest

from sphinx.application import Sphinx

import moodle_docs_theme


def build_toggle(extra_conf: str) -> str:
    """Compila um projeto mínimo e devolve a tag de abertura do botão de tema."""
    with tempfile.TemporaryDirectory() as tmp:
        src = os.path.join(tmp, "src")
        os.makedirs(src)
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
    start = html.index('id="theme-toggle"')
    return html[html.rindex("<button", 0, start):html.index(">", start) + 1]


class TestThemeToggle(unittest.TestCase):

    def test_english_labels_name_the_action(self):
        button = build_toggle('language = "en"\n')
        self.assertIn('aria-label="Dark mode"', button)
        self.assertIn('title="Dark mode"', button)
        self.assertIn('data-label-to-light="Light mode"', button)
        self.assertIn('data-label-to-dark="Dark mode"', button)

    def test_portuguese_labels_name_the_action(self):
        button = build_toggle('language = "pt_BR"\n')
        self.assertIn('aria-label="Modo escuro"', button)
        self.assertIn('data-label-to-light="Modo claro"', button)

    def test_dark_mode_disabled_hides_button(self):
        with self.assertRaises(ValueError):
            build_toggle('html_theme_options = {"enable_dark_mode": False}\n')


if __name__ == "__main__":
    unittest.main()
