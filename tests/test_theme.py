"""
Testes unitários para o tema moodle_docs_theme.
"""
import os
import unittest
from unittest.mock import MagicMock

import moodle_docs_theme


class TestMoodleDocsTheme(unittest.TestCase):

    def test_version(self):
        self.assertIsNotNone(moodle_docs_theme.__version__)
        self.assertTrue(len(moodle_docs_theme.__version__) > 0)

    def test_get_html_theme_path(self):
        theme_path = moodle_docs_theme.get_html_theme_path()
        self.assertTrue(os.path.isdir(theme_path))
        self.assertTrue(os.path.exists(os.path.join(theme_path, "theme.conf")))
        self.assertTrue(os.path.exists(os.path.join(theme_path, "layout.html")))

    def test_setup(self):
        mock_app = MagicMock()
        result = moodle_docs_theme.setup(mock_app)

        mock_app.add_html_theme.assert_called_once_with(
            "moodle_docs_theme", moodle_docs_theme.get_html_theme_path()
        )
        self.assertEqual(mock_app.add_css_file.call_count, 2)
        self.assertEqual(mock_app.add_js_file.call_count, 1)
        self.assertTrue(result["parallel_read_safe"])
        self.assertTrue(result["parallel_write_safe"])

    def test_validate_github_actions_config_skipped_locally(self):
        # Se GITHUB_ACTIONS não for 'true', não deve validar/lançar erro
        old_val = os.environ.pop("GITHUB_ACTIONS", None)
        old_run_id = os.environ.pop("GITHUB_RUN_ID", None)
        try:
            mock_app = MagicMock()
            mock_app.config.extensions = []
            # Não deve lançar exceção
            moodle_docs_theme.validate_github_actions_config(mock_app)
        finally:
            if old_val is not None:
                os.environ["GITHUB_ACTIONS"] = old_val
            if old_run_id is not None:
                os.environ["GITHUB_RUN_ID"] = old_run_id

    def test_validate_github_actions_config_raises_when_missing(self):
        from sphinx.errors import ExtensionError

        old_val = os.environ.get("GITHUB_ACTIONS")
        try:
            os.environ["GITHUB_ACTIONS"] = "true"
            mock_app = MagicMock()
            mock_app.config.extensions = ["sphinx.ext.autodoc"]

            with self.assertRaises(ExtensionError) as ctx:
                moodle_docs_theme.validate_github_actions_config(mock_app)

            self.assertIn("moodle_docs_theme", str(ctx.exception))
            self.assertIn("sphinx.ext.githubpages", str(ctx.exception))
        finally:
            if old_val is not None:
                os.environ["GITHUB_ACTIONS"] = old_val
            else:
                os.environ.pop("GITHUB_ACTIONS", None)


if __name__ == "__main__":
    unittest.main()
