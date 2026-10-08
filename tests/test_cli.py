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
        self.assertTrue((docs_dir / "index.html").exists())
        self.assertTrue((docs_dir / "requirements.txt").exists())
        self.assertTrue((target_dir / ".github" / "workflows" / "docs.yml").exists())

        # Verifica pasta en
        en_dir = docs_dir / "en"
        self.assertTrue((en_dir / "conf.py").exists())
        self.assertTrue((en_dir / "index.rst").exists())
        self.assertTrue((en_dir / "installation.rst").exists())
        self.assertTrue((en_dir / "configuration.rst").exists())
        self.assertTrue((en_dir / "usage.rst").exists())

        # Verifica pasta pt-br
        pt_dir = docs_dir / "pt-br"
        self.assertTrue((pt_dir / "conf.py").exists())
        self.assertTrue((pt_dir / "index.rst").exists())
        self.assertTrue((pt_dir / "installation.rst").exists())
        self.assertTrue((pt_dir / "configuration.rst").exists())
        self.assertTrue((pt_dir / "usage.rst").exists())

        # Verifica conteúdo renderizado
        conf_en = (en_dir / "conf.py").read_text(encoding="utf-8")
        self.assertIn('project = "tool_sample"', conf_en)
        self.assertIn('"github_repo": "moodle-by-kelsoncm/tool_sample"', conf_en)
        self.assertIn('language = "en"', conf_en)

        conf_pt = (pt_dir / "conf.py").read_text(encoding="utf-8")
        self.assertIn('project = "tool_sample"', conf_pt)
        self.assertIn('language = "pt_BR"', conf_pt)

    def test_cli_init_single_lang(self):
        target_dir = Path(self.test_dir) / "tool_single"
        target_dir.mkdir()

        exit_code = main(["init", str(target_dir), "--single-lang"])
        self.assertEqual(exit_code, 0)

        docs_dir = target_dir / "docs"
        self.assertTrue((docs_dir / "conf.py").exists())
        self.assertTrue((docs_dir / "index.md").exists())
        self.assertTrue((docs_dir / "requirements.txt").exists())

    def test_cli_init_custom_options(self):
        target_dir = Path(self.test_dir) / "atto_custom"
        target_dir.mkdir()

        exit_code = main([
            "init",
            str(target_dir),
            "--project-name", "moodle-atto_custom",
            "--repo", "moodle-by-kelsoncm/atto_custom",
            "--tagline", "Custom Atto plugin description",
            "--tagline-en", "English description",
            "--tagline-pt", "Descrição em português",
            "--version-str", "2.1.0",
            "--no-workflow",
        ])
        self.assertEqual(exit_code, 0)

        docs_dir = target_dir / "docs"
        conf_en = (docs_dir / "en" / "conf.py").read_text(encoding="utf-8")
        self.assertIn('project = "moodle-atto_custom"', conf_en)
        self.assertIn('release = "2.1.0"', conf_en)
        self.assertIn('English description', conf_en)

        conf_pt = (docs_dir / "pt-br" / "conf.py").read_text(encoding="utf-8")
        self.assertIn('Descrição em português', conf_pt)

        # Sem workflow
        self.assertFalse((target_dir / ".github" / "workflows" / "docs.yml").exists())

    def test_cli_init_skip_existing_without_force(self):
        target_dir = Path(self.test_dir) / "existing_repo"
        target_dir.mkdir()
        docs_dir = target_dir / "docs"
        en_dir = docs_dir / "en"
        en_dir.mkdir(parents=True)
        (en_dir / "conf.py").write_text("existing content", encoding="utf-8")

        exit_code = main(["init", str(target_dir)])
        self.assertEqual(exit_code, 0)

        self.assertEqual((en_dir / "conf.py").read_text(encoding="utf-8"), "existing content")

        # Com --force deve sobrescrever
        exit_code = main(["init", str(target_dir), "--force"])
        self.assertEqual(exit_code, 0)
        self.assertIn("moodle_docs_theme", (en_dir / "conf.py").read_text(encoding="utf-8"))

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
