"""
Template files for moodle-docs-theme.
This file marks the package and provides helper to locate template files.
"""
import os


def get_template_dir() -> str:
    """Return the absolute path to the template directory."""
    return os.path.join(os.path.abspath(os.path.dirname(__file__)))
