#!/usr/bin/env python
from setuptools import setup, find_namespace_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="moodle-docs-theme",
    version="0.2.1",
    author="KelsonCM",
    author_email="kelsoncm@gmail.com",
    description="Um tema Sphinx reutilizável inspirado visualmente na documentação oficial do Moodle (docs.moodle.org)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/moodle-by-kelsoncm/moodle-docs-theme",
    install_requires=[
        "sphinx>=4.0",
        "myst-parser>=2.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "pytest-cov",
        ],
    },
    packages=find_namespace_packages(include=["moodle_docs_theme*"]),
    include_package_data=True,
    package_data={
        "moodle_docs_theme": [
            "*.html", "theme.conf", "theme.toml",
            "static/css/*.css", "static/js/*.js",
            "template/docs/*", "template/workflows/*",
        ],
    },
    entry_points={
        "console_scripts": [
            "moodle-docs-theme = moodle_docs_theme.cli:main",
        ],
        "sphinx.html_themes": [
            "moodle_docs_theme = moodle_docs_theme",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Documentation",
        "Topic :: Documentation :: Sphinx",
        "Topic :: Software Development :: Documentation",
    ],
    python_requires=">=3.8",
)
