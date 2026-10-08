# Template de Documentação — moodle-docs-theme

Este diretório contém os arquivos de modelo padrão para estruturar a documentação de qualquer repositório de plugin ou projeto da organização **[moodle-by-kelsoncm](https://github.com/moodle-by-kelsoncm)**.

## 🚀 Como Utilizar

### Opção 1: Via CLI `moodle-docs-theme` (Recomendado)

No diretório raiz do plugin que deseja documentar:

```bash
# Instale o moodle-docs-theme
pip install moodle-docs-theme

# Inicialize o template (autodetecta o nome e o tipo do plugin)
moodle-docs-theme init

# Ou especificando argumentos
moodle-docs-theme init . --project-name "moodle-atto_justify" --repo "moodle-by-kelsoncm/atto_justify"
```

O comando irá gerar:
- `docs/conf.py` (pré-configurado com o tema e suporte a Markdown via `myst-parser`)
- `docs/index.md` (página inicial padrão com visão geral e tópicos)
- `docs/installation.md` (guia de instalação)
- `docs/configuration.md` (guia de configuração)
- `docs/usage.md` (guia de uso)
- `docs/requirements.txt` (dependências de documentação)
- `.github/workflows/docs.yml` (workflow para build e deploy automático no GitHub Pages)

### Opção 2: Cópia Manual

Copie os diretórios `docs/` e `.github/workflows/docs.yml` deste template para a raiz do repositório de destino e ajuste as variáveis `{{ ... }}` no `conf.py` e nos arquivos `.md`.

---

## 🛠️ Gerando a Documentação Localmente

```bash
moodle-docs-theme build
```

Os arquivos HTML serão gerados em `docs/_build/html/`.
