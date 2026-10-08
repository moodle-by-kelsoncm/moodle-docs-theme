#!/usr/bin/env python3
"""
Script utilitário para gerar a própria documentação do moodle-docs-theme.

Uso:
    python build_docs.py [--clean] [--builder html]
"""
import sys
from moodle_docs_theme.cli import main

if __name__ == "__main__":
    args = ["build", "docs", "docs/_build/html"] + sys.argv[1:]
    sys.exit(main(args))
