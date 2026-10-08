Configuration
=============

All options are passed via ``html_theme_options`` in the ``conf.py`` file of your project:

.. code-block:: python

   html_theme_options = {
       "primary_color": "#6c336d",
       "secondary_color": "#f98012",
       "project_name": "My Moodle Plugin",
       "logo": "logo.png",
       "logo_height": "32px",
       "tagline": "Plugin documentation",
       "github_url": "https://github.com/org/repo",
       "github_repo": "org/repo",
       "github_version": "main",
       "doc_path": "docs/en/",
       "show_edit_on_github": True,
       "enable_dark_mode": True,
       "enable_language_selector": True,
       "navigation_links": "Home|index, Installation|installation, Usage|usage",
   }

Available options
-----------------

.. list-table::
   :header-rows: 1

   * - Option
     - Default
     - Description
   * - ``primary_color``
     - ``#6c336d``
     - Primary brand color (purple), used for section titles and accents.
   * - ``secondary_color``
     - ``#f98012``
     - Accent color (Moodle orange), used for header stripe and active tabs.
   * - ``project_name``
     - ``project``
     - Display name shown in the top header.
   * - ``logo``
     - ``""``
     - Logo filename located inside ``_static/``.
   * - ``logo_height``
     - ``32px``
     - Logo display height in header.
   * - ``github_url``
     - ``""``
     - Full URL to GitHub repository.
   * - ``github_repo``
     - ``""``
     - Repository in ``owner/repo`` format for edit links.
   * - ``github_version``
     - ``main``
     - Target git branch for edit links.
   * - ``doc_path``
     - ``docs/``
     - Relative path to docs directory in git repository.
   * - ``show_edit_on_github``
     - ``True``
     - Show "Edit on GitHub" button in the navigation.
   * - ``enable_dark_mode``
     - ``True``
     - Enable the light/dark mode theme toggle button.
   * - ``enable_language_selector``
     - ``True``
     - Enable bilingual flag switcher in the header (USA and Brazil flags).
   * - ``navigation_links``
     - ``""``
     - Links in format ``"Title|target, Title2|target2"``.

Overriding styles
-----------------

Each project may override CSS variables by placing a custom stylesheet in
``_static/css/custom.css`` and referencing it in ``html_css_files``:

.. code-block:: css

   :root {
     --moodle-primary: #4a2350;
     --moodle-accent: #ff7a00;
   }
