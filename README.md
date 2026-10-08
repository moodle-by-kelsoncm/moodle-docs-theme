# moodle-docs-theme

Tema sphinx baseado do Moodle Docs.

Um **tema Sphinx reutilizável** inspirado visualmente na documentação oficial do Moodle
([docs.moodle.org](https://docs.moodle.org/)), criado para temas e plugins Moodle
mantidos por organizações no GitHub. Mantém a mesma identidade visual — cabeçalho claro
com faixa de destaque laranja, títulos em roxo, links em azul — em toda a documentação
da sua organização.

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Sphinx](https://img.shields.io/badge/sphinx-4.0%2B-green)
![CI & Docs](https://github.com/moodle-by-kelsoncm/moodle-docs-theme/actions/workflows/publish-pypi.yml/badge.svg)
![License](https://img.shields.io/badge/license-BSD--3--Clause-blue)

---

## Recursos principais

- **Design inspirado no MoodleDocs**: cabeçalho claro com faixa de destaque laranja
  (`#f98012`), títulos em roxo (`#6c336d`), links em azul (`#3366cc`) — a mesma
  linguagem visual do docs.moodle.org.
- **Internacionalização bilíngue**: suporte nativo aos idiomas Inglês (`en`, default) e Português do Brasil (`pt-br`), com seletor de bandeiras (EUA e Brasil) no cabeçalho e roteador inteligente `index.html` na raiz.
- **Modo escuro**: alternância de tema claro/escuro com detecção de preferência do
  sistema e persistência em `localStorage`.
- **Customização simples**: cores, logotipo, fontes e links de navegação configuráveis
  via `conf.py`, sem editar CSS.
- **Blocos de código interativos**: botão para copiar snippets com um clique.
- **Editar no GitHub**: link automático para editar a página no repositório
  correspondente.
- **100% responsivo**: menu adaptado para dispositivos móveis e desktop.
- **Automação GitHub Actions**: build e deploy de docs no GitHub Pages, publicação no
  PyPI via *Trusted Publishing* a cada release.

---

## Instalação

### Via PyPI

```bash
pip install moodle-docs-theme
```

### Instalação direta do GitHub

```bash
pip install git+https://github.com/moodle-by-kelsoncm/moodle-docs-theme.git
```

### Desenvolvimento local

```bash
git clone https://github.com/moodle-by-kelsoncm/moodle-docs-theme.git
cd moodle-docs-theme
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

---

## Configuração básica no `conf.py`

No arquivo `conf.py` da documentação do seu tema ou plugin Moodle, adicione:

```python
import moodle_docs_theme

html_theme = "moodle_docs_theme"
html_theme_path = [moodle_docs_theme.get_html_theme_path()]

extensions = [
    "sphinx.ext.githubpages",
]

html_theme_options = {
    "primary_color": "#6c336d",
    "secondary_color": "#f98012",
    "project_name": "Meu Plugin Moodle",
    "logo": "logo.png",
    "logo_height": "32px",
    "github_url": "https://github.com/usuario/meu-plugin",
    "github_repo": "usuario/meu-plugin",
    "github_version": "main",
    "doc_path": "docs/",
    "show_edit_on_github": True,
    "enable_dark_mode": True,
    "navigation_links": "Início|index.html, Instalação|installation.html",
}

html_static_path = ["_static"]
```

Veja a [documentação completa](https://moodle-by-kelsoncm.github.io/moodle-docs-theme/)
para a lista completa de opções.

---

## Template de documentação para repositórios

O `moodle-docs-theme` inclui um template completo e padronizado para estruturar a documentação de qualquer repositório ou plugin Moodle da organização:

### Inicialização via CLI

```bash
# No diretório raiz do plugin
moodle-docs-theme init
```

O comando detecta o tipo de plugin, configura o `docs/conf.py` (com suporte a Markdown nativo via `myst-parser`), cria as páginas modelo (`index.md`, `installation.md`, `configuration.md`, `usage.md`), `docs/requirements.txt` e o workflow do GitHub Actions em `.github/workflows/docs.yml`.

### Compilando a documentação

Para compilar a documentação do projeto atual:

```bash
moodle-docs-theme build
```

Ou para compilar a documentação do próprio tema:

```bash
python build_docs.py
```

---

## Estrutura do repositório

```
moodle-docs-theme/
├── .github/
│   └── workflows/
│       └── publish-pypi.yml   # Integração contínua, docs (Pages) e publicação (PyPI)
├── docs/                      # Documentação oficial do tema
│   ├── conf.py
│   ├── index.rst
│   ├── installation.rst
│   ├── configuration.rst
│   └── template.rst           # Guia de uso do template
├── moodle_docs_theme/         # Código fonte do tema Sphinx
│   ├── static/
│   │   ├── css/
│   │   │   ├── base.css
│   │   │   └── colors.css
│   │   └── js/
│   │       └── theme.js
│   ├── template/              # Arquivos modelo do template de documentação
│   │   ├── docs/
│   │   └── workflows/
│   ├── cli.py                 # CLI moodle-docs-theme (init, build)
│   ├── __main__.py
│   ├── layout.html
│   ├── page.html
│   ├── searchbox.html
│   ├── breadcrumbs.html
│   ├── theme.conf
│   ├── theme.toml
│   └── __init__.py
├── template/                  # Template de documentação exposto na raiz
├── tests/                     # Testes automatizados (pytest)
├── build_docs.py              # Script para gerar a própria documentação
├── setup.py
├── pyproject.toml
├── MANIFEST.in
├── LICENSE
└── README.md
```

---

## Compilando a documentação localmente

```bash
pip install -e .
python build_docs.py --clean
```


---

## Licença

Este projeto está licenciado sob a Licença BSD 3-Clause. Consulte o arquivo
[LICENSE](LICENSE) para mais detalhes.
