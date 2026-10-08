Reusable Documentation Template
=================================

``moodle-docs-theme`` provides a **standard bilingual documentation template** ready to use
across all plugins and repositories of the `Moodle by KelsonCM <https://github.com/moodle-by-kelsoncm>`_ organization.

The template standardizes:

* Bilingual structure with English (default) in ``docs/en/`` and Brazilian Portuguese in ``docs/pt-br/``.
* Automatic language router at ``docs/index.html`` redirecting users according to browser preferences or stored choice.
* Standard reStructuredText pages (``index.rst``, ``installation.rst``, ``configuration.rst``, ``usage.rst``).
* Python requirements in ``docs/requirements.txt``.
* Automated GitHub Actions workflow (``.github/workflows/docs.yml``) for building and deploying to GitHub Pages.

How to Use the Template
-----------------------

Via CLI ``moodle-docs-theme init`` (Recommended)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To initialize documentation in any plugin repository:

1. Navigate to the repository root directory:

.. code-block:: bash

   cd /path/to/plugin_repository

2. Run the ``init`` command:

.. code-block:: bash

   moodle-docs-theme init

The CLI automatically detects directory names, infers plugin categories in Moodle,
and creates the complete bilingual documentation structure.

Available CLI Options
^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Option
     - Description
   * - ``target_dir``
     - Target repository root path (default: current directory ``.``).
   * - ``--project-name``
     - Project name (default: directory name).
   * - ``--repo``
     - GitHub repository path (default: ``moodle-by-kelsoncm/<dirname>``).
   * - ``--tagline-en``
     - English tagline for documentation header.
   * - ``--tagline-pt``
     - Portuguese tagline for documentation header.
   * - ``--version-str``
     - Version string (default: ``1.0.0``).
   * - ``--force``
     - Overwrite existing template files.
   * - ``--single-lang``
     - Generate legacy single-language template directly in ``docs/``.
   * - ``--no-workflow``
     - Skip generating ``.github/workflows/docs.yml``.
