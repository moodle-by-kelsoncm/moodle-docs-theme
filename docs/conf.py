import moodle_docs_theme

project = "moodle-docs-theme"
copyright = "2026, Contribuições de KelsonCM à comunidade Moodle"
author = "KelsonCM"
release = moodle_docs_theme.__version__

extensions = ["sphinx.ext.githubpages"]

templates_path = []
exclude_patterns = ["_build"]

language = "pt_BR"

html_theme = "moodle_docs_theme"
html_theme_path = [moodle_docs_theme.get_html_theme_path()]

html_theme_options = {
    "primary_color": "#6c336d",
    "secondary_color": "#f98012",
    "project_name": "moodle-docs-theme",
    "tagline": "Tema Sphinx inspirado no docs.moodle.org",
    "github_url": "https://github.com/moodle-by-kelsoncm/moodle-docs-theme",
    "github_repo": "moodle-by-kelsoncm/moodle-docs-theme",
    "github_version": "main",
    "doc_path": "docs/",
    "show_edit_on_github": True,
    "enable_dark_mode": True,
    "navigation_links": "Início|index, Instalação|installation, Configuração|configuration",
}

html_static_path = []
