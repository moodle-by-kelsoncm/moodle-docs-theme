"""
Testes unitários para o CLI do moodle-docs-theme.
"""
import os
import shutil
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from moodle_docs_theme.cli import (
    _infer_plugin_info,
    _render_template,
    build_parser,
    main,
)


class TestMoodleDocsThemeCLI(unittest.TestCase):

    def setUp(self):
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.test_dir, ignore_errors=True)

    def test_infer_plugin_info(self):
        self.assertEqual(_infer_plugin_info("atto_justify"), ("lib/editor/atto/plugins", "justify"))
        self.assertEqual(_infer_plugin_info("tiny_fontfamily"), ("lib/editor/tiny/plugins", "fontfamily"))
        self.assertEqual(_infer_plugin_info("tool_ribbons"), ("admin/tool", "ribbons"))
        self.assertEqual(_infer_plugin_info("block_recommendation"), ("blocks", "recommendation"))
        self.assertEqual(_infer_plugin_info("mod_imagemap"), ("mod", "imagemap"))
        self.assertEqual(_infer_plugin_info("local_tinytoolbar"), ("local", "tinytoolbar"))
        self.assertEqual(_infer_plugin_info("format_timeline"), ("course/format", "timeline"))
        self.assertEqual(_infer_plugin_info("profilefield_json"), ("user/profile/field", "json"))
        self.assertEqual(_infer_plugin_info("theme_boost"), ("theme", "boost"))
        self.assertEqual(_infer_plugin_info("custom_repo"), ("local", "custom_repo"))

    def test_render_template(self):
        tpl_path = Path(self.test_dir) / "template.txt"
        tpl_path.write_text("Hello {{ name }}! Repo: {{ repo }}", encoding="utf-8")
        result = _render_template(tpl_path, {"name": "World", "repo": "moodle/org"})
        self.assertEqual(result, "Hello World! Repo: moodle/org")

    def test_cli_init_default(self):
        target_dir = Path(self.test_dir) / "tool_sample"
        target_dir.mkdir()

        exit_code = main(["init", str(target_dir)])
        self.assertEqual(exit_code, 0)

        docs_dir = target_dir / "docs"
        self.assertTrue((docs_dir / "conf.py").exists())
        self.assertTrue((docs_dir / "index.md").exists())
        self.assertTrue((docs_dir / "installation.md").exists())
        self.assertTrue((docs_dir / "configuration.md").exists())
        self.assertTrue((docs_dir / "usage.md").exists())
        self.assertTrue((docs_dir / "requirements.txt").exists())
        self.assertTrue((target_dir / ".github" / "workflows" / "docs.yml").exists())

        # Verifica conteúdo renderizado
        conf_content = (docs_dir / "conf.py").read_text(encoding="utf-8")
        self.assertIn('project = "tool_sample"', conf_content)
        self.assertIn('"github_repo": "moodle-by-kelsoncm/tool_sample"', conf_content)
        self.assertIn('"moodle_docs_theme"', conf_content)

    def test_cli_init_custom_options(self):
        target_dir = Path(self.test_dir) / "atto_custom"
        target_dir.mkdir()

        exit_code = main([
            "init",
            str(target_dir),
            "--project-name", "moodle-atto_custom",
            "--repo", "moodle-by-kelsoncm/atto_custom",
            "--tagline", "Custom Atto plugin description",
            "--version-str", "2.1.0",
            "--no-workflow",
        ])
        self.assertEqual(exit_code, 0)

        docs_dir = target_dir / "docs"
        conf_content = (docs_dir / "conf.py").read_text(encoding="utf-8")
        self.assertIn('project = "moodle-atto_custom"', conf_content)
        self.assertIn('release = "2.1.0"', conf_content)
        self.assertIn('Custom Atto plugin description', conf_content)

        # Sem workflow
        self.assertFalse((target_dir / ".github" / "workflows" / "docs.yml").exists())

    def test_cli_init_skip_existing_without_force(self):
        target_dir = Path(self.test_dir) / "existing_repo"
        target_dir.mkdir()
        docs_dir = target_dir / "docs"
        docs_dir.mkdir()
        (docs_dir / "conf.py").write_text("existing content", encoding="utf-8")

        exit_code = main(["init", str(target_dir)])
        self.assertEqual(exit_code, 0)

        self.assertEqual((docs_dir / "conf.py").read_text(encoding="utf-8"), "existing content")

        # Com --force deve sobrescrever
        exit_code = main(["init", str(target_dir), "--force"])
        self.assertEqual(exit_code, 0)
        self.assertIn("moodle_docs_theme", (docs_dir / "conf.py").read_text(encoding="utf-8"))

    def test_cli_build_nonexistent_directory(self):
        nonexistent = str(Path(self.test_dir) / "nao_existe")
        exit_code = main(["build", nonexistent])
        self.assertEqual(exit_code, 1)

    def test_cli_build_missing_conf_py(self):
        empty_dir = str(Path(self.test_dir) / "empty")
        os.makedirs(empty_dir)
        exit_code = main(["build", empty_dir])
        self.assertEqual(exit_code, 1)

    def test_parser_version(self):
        parser = build_parser()
        with self.assertRaises(SystemExit) as ctx:
            parser.parse_args(["--version"])
        self.assertEqual(ctx.exception.code, 0)


if __name__ == "__main__":
    unittest.main()
