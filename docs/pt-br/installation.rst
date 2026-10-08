Instalação
===========

Via PyPI
--------

.. code-block:: bash

   pip install moodle-docs-theme

Instalação direta do GitHub
-----------------------------

.. code-block:: bash

   pip install git+https://github.com/moodle-by-kelsoncm/moodle-docs-theme.git

Ativando no ``conf.py``
-------------------------

.. code-block:: python

   import moodle_docs_theme

   html_theme = "moodle_docs_theme"
   html_theme_path = [moodle_docs_theme.get_html_theme_path()]

   extensions = [
       "sphinx.ext.githubpages",
   ]

O ``sphinx.ext.githubpages`` garante a geração do arquivo ``.nojekyll``, necessário para
o GitHub Pages não bloquear a pasta ``_static/``.
