# Instalação — {{ project_name }}

Este guia descreve os passos para instalar o **{{ project_name }}** no seu ambiente Moodle.

---

## Requisitos

- **Moodle**: 4.0 ou superior (recomendado Moodle 4.5+).
- **PHP**: 8.1 ou superior (recomendado PHP 8.3+).
- Permissões de escrita no diretório do plugin durante a instalação.

---

## Métodos de Instalação

### 1. Via Git (Recomendado para Desenvolvimento)

Clone o repositório diretamente no diretório apropriado do seu Moodle:

```bash
cd /caminho/do/moodle/{{ plugin_path }}
git clone {{ github_url }}.git {{ plugin_dir_name }}
```

### 2. Via Pacote ZIP

1. Baixe o arquivo `.zip` da release mais recente no [GitHub Releases]({{ github_url }}/releases).
2. Extraia o conteúdo na pasta correspondente do Moodle (`{{ plugin_path }}/{{ plugin_dir_name }}`).
3. Acesse a administração do Moodle (*Administração do Site > Notificações*) para concluir a instalação do banco de dados.

---

## Pós-Instalação

Após a instalação, purgue os caches do Moodle:

```bash
php admin/cli/purge_caches.php
```
