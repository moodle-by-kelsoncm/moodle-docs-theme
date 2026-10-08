"""
Sphinx configuration for {{ project_name }} (English).
Documentation generated with moodle-docs-theme.
"""
import os
import sys
import moodle_docs_theme

project = "{{ project_name }}"
copyright = "{{ year }}, KelsonCM contributions to Moodle community"
author = "KelsonCM"
release = "{{ version }}"

extensions = [
    "sphinx.ext.githubpages",
    "moodle_docs_theme",
]

templates_path = []
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

language = "en"

html_theme = "moodle_docs_theme"
html_theme_path = [moodle_docs_theme.get_html_theme_path()]

html_theme_options = {
    "primary_color": "#6c336d",
    "secondary_color": "#f98012",
    "project_name": "{{ project_name }}",
    "tagline": "{{ tagline_en }}",
    "github_url": "{{ github_url }}",
    "github_repo": "{{ github_repo }}",
    "github_version": "main",
    "doc_path": "docs/en/",
    "show_edit_on_github": True,
    "enable_dark_mode": True,
    "enable_language_selector": True,
    "navigation_links": "Home|index, Installation|installation, Configuration|configuration, Usage|usage",
}

html_static_path = []
