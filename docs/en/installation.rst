Installation
============

Via PyPI
--------

.. code-block:: bash

   pip install moodle-docs-theme

Direct installation from GitHub
-------------------------------

.. code-block:: bash

   pip install git+https://github.com/moodle-by-kelsoncm/moodle-docs-theme.git

Enabling in ``conf.py``
-----------------------

.. code-block:: python

   import moodle_docs_theme

   html_theme = "moodle_docs_theme"
   html_theme_path = [moodle_docs_theme.get_html_theme_path()]

   extensions = [
       "sphinx.ext.githubpages",
   ]

``sphinx.ext.githubpages`` ensures generation of the ``.nojekyll`` file required by GitHub Pages
to serve assets within ``_static/``.
