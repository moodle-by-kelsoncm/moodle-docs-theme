Instalação
==========

Requisitos
----------

- Moodle 4.1, 4.2, 4.3, 4.4 ou superior
- PHP 8.1 ou superior

Instalação via Git
------------------

Clone o repositório na sua instalação Moodle dentro do diretório ``{{ plugin_path }}/{{ plugin_dir_name }}``:

.. code-block:: bash

   cd /path/to/moodle/{{ plugin_path }}
   git clone {{ github_url }}.git {{ plugin_dir_name }}

Concluindo a Instalação
-----------------------

1. Acesse o Moodle com uma conta de administrador.
2. Siga as instruções na tela para concluir a atualização do banco de dados do plugin.
3. Ou execute o comando via terminal CLI:

.. code-block:: bash

   php admin/cli/upgrade.php
