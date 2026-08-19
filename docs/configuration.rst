Configuração
=============

Todas as opções são passadas via ``html_theme_options`` no ``conf.py`` do projeto que
consome o tema:

.. code-block:: python

   html_theme_options = {
       "primary_color": "#6c336d",
       "secondary_color": "#f98012",
       "project_name": "Meu Plugin Moodle",
       "logo": "logo.png",
       "logo_height": "32px",
       "tagline": "Documentação do meu plugin",
       "github_url": "https://github.com/org/repo",
       "github_repo": "org/repo",
       "github_version": "main",
       "doc_path": "docs/",
       "show_edit_on_github": True,
       "enable_dark_mode": True,
       "navigation_links": "Início|index, Instalação|installation, Uso|usage",
   }

Opções disponíveis
--------------------

.. list-table::
   :header-rows: 1

   * - Opção
     - Padrão
     - Descrição
   * - ``primary_color``
     - ``#6c336d``
     - Cor primária (roxo), usada nos títulos de seção e destaques.
   * - ``secondary_color``
     - ``#f98012``
     - Cor de destaque (laranja Moodle), usada na faixa do cabeçalho e abas ativas.
   * - ``project_name``
     - ``project``
     - Nome exibido no cabeçalho ao lado da logo.
   * - ``logo``
     - ``""``
     - Nome do arquivo de logo dentro de ``_static/``.
   * - ``logo_height``
     - ``32px``
     - Altura do logotipo no cabeçalho.
   * - ``github_url``
     - ``""``
     - URL completa do repositório no GitHub.
   * - ``github_repo``
     - ``""``
     - Repositório no formato ``owner/repo`` para o link "Editar no GitHub".
   * - ``github_version``
     - ``main``
     - Branch padrão do GitHub para o link de edição.
   * - ``doc_path``
     - ``docs/``
     - Caminho do diretório de documentos no repositório.
   * - ``show_edit_on_github``
     - ``True``
     - Exibe o botão "Editar no GitHub" na barra de navegação.
   * - ``enable_dark_mode``
     - ``True``
     - Habilita o botão de alternância para o Modo Escuro.
   * - ``navigation_links``
     - ``""``
     - Links no formato ``"Título|url, Título2|url2"``.

Sobrescrevendo estilos
------------------------

Cada projeto pode sobrescrever as variáveis CSS globais criando
``_static/css/custom.css`` e listando-o em ``html_css_files``:

.. code-block:: css

   :root {
     --moodle-primary: #4a2350;
     --moodle-accent: #ff7a00;
   }
