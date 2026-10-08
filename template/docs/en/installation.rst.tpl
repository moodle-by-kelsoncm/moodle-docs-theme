Installation
============

Requirements
------------

- Moodle 4.1, 4.2, 4.3, 4.4 or higher
- PHP 8.1 or higher

Installation via Git
--------------------

Clone this repository into your Moodle installation under ``{{ plugin_path }}/{{ plugin_dir_name }}``:

.. code-block:: bash

   cd /path/to/moodle/{{ plugin_path }}
   git clone {{ github_url }}.git {{ plugin_dir_name }}

Completing Installation
-----------------------

1. Access the Moodle admin interface as administrator.
2. Follow the on-screen instructions to complete the plugin database upgrade.
3. Or run the CLI upgrade script:

.. code-block:: bash

   php admin/cli/upgrade.php
