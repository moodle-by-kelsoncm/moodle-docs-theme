Template de Documentação Reutilizável
======================================

O ``moodle-docs-theme`` disponibiliza um **template padrão de documentação** pronto para ser
utilizado em todos os plugins e repositórios da organização `moodle-by-kelsoncm <https://github.com/moodle-by-kelsoncm>`_.

O template padroniza:

* Configuração Sphinx (``docs/conf.py``) pré-configurada com o tema e suporte a Markdown (via ``myst-parser``).
* Páginas padrão em Markdown (``index.md``, ``installation.md``, ``configuration.md``, ``usage.md``).
* Dependências necessárias em ``docs/requirements.txt``.
* Workflow automatizado do GitHub Actions (``.github/workflows/docs.yml``) para build e deploy no GitHub Pages.

Como Usar o Template
--------------------

Via CLI ``moodle-docs-theme init`` (Recomendado)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Para adicionar a estrutura de documentação completa em qualquer plugin ou repositório:

1. Acesse o diretório do repositório:

.. code-block:: bash

   cd /caminho/do/seu-plugin

2. Execute o comando ``init``:

.. code-block:: bash

   moodle-docs-theme init

O CLI detecta automaticamente o nome da pasta, infere o caminho correspondente do plugin no Moodle
(por exemplo, ``lib/editor/atto/plugins`` para ``atto_*`` ou ``admin/tool`` para ``tool_*``) e configura
todos os arquivos necessários.

Opções Disponíveis no Comando ``init``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Opção
     - Descrição
   * - ``target_dir``
     - Diretório raiz onde a documentação será gerada (padrão: diretório atual ``.``).
   * - ``--project-name``
     - Nome legível do projeto (padrão: nome do diretório).
   * - ``--repo``
     - Caminho no GitHub (padrão: ``moodle-by-kelsoncm/<nome_pasta>``).
   * - ``--tagline``
     - Subtítulo ou slogan exibido no cabeçalho da documentação.
   * - ``--version-str``
     - Versão inicial do componente (padrão: ``1.0.0``).
   * - ``--plugin-path``
     - Caminho relativo da categoria do plugin no Moodle.
   * - ``--force``
     - Sobrescreve arquivos existentes que já estejam na pasta ``docs/``.
   * - ``--no-workflow``
     - Não cria o arquivo de automação ``.github/workflows/docs.yml``.

Exemplo com Parâmetros Customizados
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   moodle-docs-theme init . \
       --project-name "moodle-atto_justify" \
       --repo "moodle-by-kelsoncm/atto_justify" \
       --tagline "Botão de texto justificado para o editor Atto" \
       --version-str "1.2.0"

Estrutura de Arquivos Gerada
----------------------------

Após executar o comando ``init``, a seguinte árvore de diretórios é criada:

.. code-block:: text

   seu-plugin/
   ├── .github/
   │   └── workflows/
   │       └── docs.yml           # Workflow CI/CD de build e deploy no GitHub Pages
   └── docs/
       ├── conf.py                # Configuração Sphinx com moodle_docs_theme e myst_parser
       ├── index.md               # Página inicial do plugin
       ├── installation.md        # Guia de instalação manual e via Git
       ├── configuration.md       # Tabela de configurações administrativas
       ├── usage.md               # Instruções e casos de uso
       └── requirements.txt       # Dependências Python para compilar a documentação

Gerando a Documentação Localmente
---------------------------------

Para compilar os arquivos HTML da documentação em seu ambiente local:

.. code-block:: bash

   moodle-docs-theme build docs docs/_build/html

Ou simplesmente:

.. code-block:: bash

   moodle-docs-theme build

Os arquivos compilados estarão prontos para visualização em ``docs/_build/html/index.html``.

Deploy Automático no GitHub Pages
---------------------------------

Com o arquivo ``.github/workflows/docs.yml`` gerado pelo template:

1. Acesse as configurações do seu repositório no GitHub: **Settings > Pages**.
2. Na seção **Build and deployment > Source**, selecione **GitHub Actions**.
3. A cada commit na branch ``main``, a documentação será compilada e publicada automaticamente na URL:

   ``https://moodle-by-kelsoncm.github.io/<nome-do-repositorio>/``
