"""
Sphinx configuration for {{ project_name }}.
Documentação gerada com o template moodle-docs-theme.
"""
import os
import sys
import moodle_docs_theme

# -- Informações do Projeto --------------------------------------------------
project = "{{ project_name }}"
copyright = "{{ year }}, Contribuições de KelsonCM à comunidade Moodle"
author = "KelsonCM"
release = "{{ version }}"

# -- Configuração Geral ------------------------------------------------------
extensions = [
    "sphinx.ext.githubpages",
    "moodle_docs_theme",
    "myst_parser",
]

# Suporte a arquivos reStructuredText (.rst) e Markdown (.md)
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

# Configurações do MyST-Parser (Markdown)
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "tasklist",
]
myst_heading_anchors = 3

templates_path = []
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

language = "pt_BR"

# -- Opções de Saída HTML ----------------------------------------------------
html_theme = "moodle_docs_theme"
html_theme_path = [moodle_docs_theme.get_html_theme_path()]

html_theme_options = {
    "primary_color": "#6c336d",
    "secondary_color": "#f98012",
    "project_name": "{{ project_name }}",
    "tagline": "{{ tagline }}",
    "github_url": "{{ github_url }}",
    "github_repo": "{{ github_repo }}",
    "github_version": "main",
    "doc_path": "docs/",
    "show_edit_on_github": True,
    "enable_dark_mode": True,
    "navigation_links": "Início|index, Instalação|installation, Configuração|configuration, Uso|usage",
}

html_static_path = []
