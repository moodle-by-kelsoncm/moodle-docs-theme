"""
Sphinx configuration for {{ project_name }} (Português do Brasil).
Documentação gerada com o template moodle-docs-theme.
"""
import os
import sys
import moodle_docs_theme

project = "{{ project_name }}"
copyright = "{{ year }}, Contribuições de KelsonCM à comunidade Moodle"
author = "KelsonCM"
release = "{{ version }}"

extensions = [
    "sphinx.ext.githubpages",
    "moodle_docs_theme",
]

templates_path = []
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

language = "pt_BR"

html_theme = "moodle_docs_theme"
html_theme_path = [moodle_docs_theme.get_html_theme_path()]

html_theme_options = {
    "primary_color": "#6c336d",
    "secondary_color": "#f98012",
    "project_name": "{{ project_name }}",
    "tagline": "{{ tagline_pt }}",
    "github_url": "{{ github_url }}",
    "github_repo": "{{ github_repo }}",
    "github_version": "main",
    "doc_path": "docs/pt-br/",
    "show_edit_on_github": True,
    "enable_dark_mode": True,
    "enable_language_selector": True,
    "navigation_links": "Início|index, Instalação|installation, Configuração|configuration, Uso|usage",
}

html_static_path = []
