"""
moodle_docs_theme - A reusable Sphinx HTML theme inspired by docs.moodle.org (MoodleDocs).
"""

import os
from typing import Dict, Any

__version__ = "0.1.0"


def get_html_theme_path() -> str:
    """
    Return the absolute path to the directory containing theme.conf.

    This function is maintained for backward compatibility with older Sphinx theme patterns.
    Modern Sphinx 1.6+ discovers the theme automatically via entry points.
    """
    return os.path.abspath(os.path.dirname(__file__))


def validate_github_actions_config(app: Any) -> None:
    """
    Validate Sphinx configuration when running inside GitHub Actions.

    If GITHUB_ACTIONS == 'true', ensures that:
    1. 'moodle_docs_theme' is present in app.config.extensions
    2. 'sphinx.ext.githubpages' is present in app.config.extensions

    Raises ExtensionError if requirements are not met.
    """
    is_github_actions = (
        os.environ.get("GITHUB_ACTIONS") == "true" or "GITHUB_RUN_ID" in os.environ
    )

    if not is_github_actions:
        return

    extensions = getattr(app.config, "extensions", []) or []
    missing_requirements = []

    if "moodle_docs_theme" not in extensions:
        missing_requirements.append(
            "• 'moodle_docs_theme' deve estar listado em 'extensions = [...]' no seu docs/conf.py."
        )

    if "sphinx.ext.githubpages" not in extensions:
        missing_requirements.append(
            "• 'sphinx.ext.githubpages' deve estar listado em 'extensions = [...]' no seu docs/conf.py para gerar o arquivo .nojekyll e evitar que o GitHub Pages bloqueie a pasta _static/."
        )

    if missing_requirements:
        error_msg = (
            "\n"
            "================================================================================\n"
            "[moodle_docs_theme] ERRO DE CONFIGURAÇÃO NO GITHUB ACTIONS\n"
            "================================================================================\n"
            "Foi detectada a execução dentro do ambiente GitHub Actions, mas as configurações\n"
            "obrigatórias do tema não foram encontradas no seu 'docs/conf.py':\n\n"
            + "\n".join(missing_requirements)
            + "\n\n"
            "Por favor, certifique-se de atualizar o 'docs/conf.py' do seu projeto:\n\n"
            "    extensions = [\n"
            "        'sphinx.ext.autodoc',\n"
            "        'sphinx.ext.githubpages',\n"
            "        'moodle_docs_theme',\n"
            "    ]\n\n"
            "================================================================================\n"
        )
        from sphinx.errors import ExtensionError
        raise ExtensionError(error_msg)


def setup(app: Any) -> Dict[str, Any]:
    """
    Sphinx extension setup function.

    Registers the theme with Sphinx when activated in conf.py.
    """
    theme_path = get_html_theme_path()
    app.add_html_theme("moodle_docs_theme", theme_path)

    app.add_css_file("css/colors.css")
    app.add_css_file("css/base.css")
    app.add_js_file("js/theme.js")

    app.connect("builder-inited", validate_github_actions_config)

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
