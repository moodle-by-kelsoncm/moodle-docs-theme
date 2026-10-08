"""
CLI para inicialização de templates e geração de documentação com moodle-docs-theme.
"""
from __future__ import annotations

import argparse
import datetime
import os
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Dict, Optional, Sequence

from moodle_docs_theme import __version__
from moodle_docs_theme.template import get_template_dir


def _infer_plugin_info(folder_name: str) -> tuple[str, str]:
    """
    Infer Moodle plugin path and directory name based on common prefix conventions.
    """
    prefixes: dict[str, str] = {
        "atto_": "lib/editor/atto/plugins",
        "tiny_": "lib/editor/tiny/plugins",
        "tool_": "admin/tool",
        "block_": "blocks",
        "mod_": "mod",
        "local_": "local",
        "format_": "course/format",
        "profilefield_": "user/profile/field",
        "editor_": "lib/editor",
        "theme_": "theme",
    }
    for prefix, plugin_path in prefixes.items():
        if folder_name.startswith(prefix):
            dir_name = folder_name[len(prefix):]
            return plugin_path, dir_name
    return "local", folder_name


def _render_template(template_path: Path, context: Dict[str, str]) -> str:
    """Render a template file with simple dictionary replacements."""
    content = template_path.read_text(encoding="utf-8")
    for key, value in context.items():
        placeholder = f"{{{{ {key} }}}}"
        content = content.replace(placeholder, str(value))
    return content


def cmd_init(args: argparse.Namespace) -> int:
    """
    Inicializa a estrutura de documentação no repositório de destino usando o template moodle-docs-theme.
    """
    target_path = Path(args.target_dir).resolve()
    folder_name = target_path.name

    project_name = args.project_name or folder_name
    repo_name = args.repo or f"moodle-by-kelsoncm/{folder_name}"
    github_url = f"https://github.com/{repo_name.strip('/')}"
    tagline = args.tagline or f"Documentação oficial de {project_name}"
    version = args.version or "1.0.0"
    year = str(datetime.datetime.now().year)

    inferred_path, inferred_dir = _infer_plugin_info(folder_name)
    plugin_path = args.plugin_path or inferred_path
    plugin_dir_name = args.plugin_dir_name or inferred_dir

    context: dict[str, str] = {
        "project_name": project_name,
        "repo_name": repo_name,
        "github_url": github_url,
        "github_repo": repo_name,
        "tagline": tagline,
        "version": version,
        "year": year,
        "plugin_path": plugin_path,
        "plugin_dir_name": plugin_dir_name,
    }

    template_dir = Path(get_template_dir())
    template_docs_dir = template_dir / "docs"
    target_docs_dir = target_path / "docs"

    target_docs_dir.mkdir(parents=True, exist_ok=True)

    files_to_render = [
        ("conf.py.tpl", "conf.py"),
        ("index.md.tpl", "index.md"),
        ("installation.md.tpl", "installation.md"),
        ("configuration.md.tpl", "configuration.md"),
        ("usage.md.tpl", "usage.md"),
    ]

    print(f"-> Inicializando template de documentação em: {target_path}")

    created_files: list[str] = []
    for src_name, dst_name in files_to_render:
        src_file = template_docs_dir / src_name
        dst_file = target_docs_dir / dst_name

        if dst_file.exists() and not args.force:
            print(f"   [IGNORADO] Arquivo já existe: {dst_file.relative_to(target_path)} (use --force para sobrescrever)")
            continue

        rendered = _render_template(src_file, context)
        dst_file.write_text(rendered, encoding="utf-8")
        created_files.append(str(dst_file.relative_to(target_path)))
        print(f"   [CRIADO]   {dst_file.relative_to(target_path)}")

    # requirements.txt
    req_src = template_docs_dir / "requirements.txt"
    req_dst = target_docs_dir / "requirements.txt"
    if not req_dst.exists() or args.force:
        shutil.copy2(req_src, req_dst)
        created_files.append(str(req_dst.relative_to(target_path)))
        print(f"   [CRIADO]   {req_dst.relative_to(target_path)}")
    else:
        print(f"   [IGNORADO] Arquivo já existe: {req_dst.relative_to(target_path)}")

    # Workflow do GitHub Actions
    if not args.no_workflow:
        target_workflows_dir = target_path / ".github" / "workflows"
        target_workflows_dir.mkdir(parents=True, exist_ok=True)
        wf_src = template_dir / "workflows" / "docs.yml"
        wf_dst = target_workflows_dir / "docs.yml"
        if not wf_dst.exists() or args.force:
            shutil.copy2(wf_src, wf_dst)
            created_files.append(str(wf_dst.relative_to(target_path)))
            print(f"   [CRIADO]   {wf_dst.relative_to(target_path)}")
        else:
            print(f"   [IGNORADO] Workflow já existe: {wf_dst.relative_to(target_path)}")

    print(f"\nSucesso: Template de documentação configurado ({len(created_files)} arquivos processados)!")
    print("Para gerar a documentação localmente, execute:")
    print(f"   moodle-docs-theme build {target_docs_dir.relative_to(target_path)}\n")
    return 0


def cmd_build(args: argparse.Namespace) -> int:
    """
    Compila a documentação usando Sphinx e moodle-docs-theme.
    """
    docs_dir = Path(args.docs_dir).resolve()
    output_dir = Path(args.output_dir).resolve()

    if not docs_dir.exists():
        print(f"Erro: Diretório de documentação não encontrado: '{docs_dir}'", file=sys.stderr)
        return 1

    conf_file = docs_dir / "conf.py"
    if not conf_file.exists():
        print(f"Erro: Arquivo 'conf.py' não encontrado em: '{docs_dir}'", file=sys.stderr)
        return 1

    if args.clean and output_dir.exists():
        print(f"-> Limpando diretório de saída: '{output_dir}'")
        shutil.rmtree(output_dir)

    output_dir.mkdir(parents=True, exist_ok=True)

    sphinx_cmd = [
        sys.executable,
        "-m",
        "sphinx",
        "-b",
        args.builder,
    ]

    if args.warnings_as_errors:
        sphinx_cmd.append("-W")

    sphinx_cmd.extend([str(docs_dir), str(output_dir)])

    print(f"-> Gerando documentação: '{docs_dir}' -> '{output_dir}'")
    try:
        result = subprocess.run(sphinx_cmd, check=False)
        if result.returncode == 0:
            print(f"\nDocumentação gerada com sucesso em: {output_dir}")
            index_path = output_dir / "index.html"
            if index_path.exists():
                print(f"Página inicial: {index_path}")
        else:
            print(f"\nFalha na geração da documentação (código de saída: {result.returncode})", file=sys.stderr)
        return result.returncode
    except Exception as exc:
        print(f"Erro ao executar Sphinx: {exc}", file=sys.stderr)
        return 1


def build_parser() -> argparse.ArgumentParser:
    """Build the argument parser for moodle-docs-theme CLI."""
    parser = argparse.ArgumentParser(
        prog="moodle-docs-theme",
        description="CLI do moodle-docs-theme para inicializar templates e compilar documentações.",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
        help="Exibe a versão do moodle-docs-theme.",
    )

    subparsers = parser.add_subparsers(dest="command", help="Comando a ser executado")

    # Comando: init
    init_parser = subparsers.add_parser(
        "init",
        help="Inicializa a estrutura de documentação em um repositório a partir do template padrão.",
    )
    init_parser.add_argument(
        "target_dir",
        nargs="?",
        default=".",
        help="Diretório raiz do repositório onde a documentação será inicializada (padrão: diretório atual).",
    )
    init_parser.add_argument(
        "--project-name",
        help="Nome do projeto / plugin (padrão: nome do diretório).",
    )
    init_parser.add_argument(
        "--repo",
        help="Caminho do repositório no GitHub (ex.: moodle-by-kelsoncm/atto_justify).",
    )
    init_parser.add_argument(
        "--tagline",
        help="Subtítulo ou descrição curta do projeto.",
    )
    init_parser.add_argument(
        "--version-str",
        dest="version",
        help="Versão inicial da documentação (padrão: 1.0.0).",
    )
    init_parser.add_argument(
        "--plugin-path",
        help="Caminho relativo da categoria do plugin no Moodle (ex.: lib/editor/atto/plugins).",
    )
    init_parser.add_argument(
        "--plugin-dir-name",
        help="Nome da pasta do plugin dentro da categoria (ex.: justify).",
    )
    init_parser.add_argument(
        "--force",
        action="store_true",
        help="Sobrescreve arquivos existentes caso já estejam presentes.",
    )
    init_parser.add_argument(
        "--no-workflow",
        action="store_true",
        help="Não gera o workflow do GitHub Actions em .github/workflows/docs.yml.",
    )
    init_parser.set_defaults(func=cmd_init)

    # Comando: build
    build_cmd_parser = subparsers.add_parser(
        "build",
        help="Compila a documentação com Sphinx e moodle-docs-theme.",
    )
    build_cmd_parser.add_argument(
        "docs_dir",
        nargs="?",
        default="docs",
        help="Diretório onde reside a documentação (contendo conf.py, padrão: 'docs').",
    )
    build_cmd_parser.add_argument(
        "output_dir",
        nargs="?",
        default="docs/_build/html",
        help="Diretório de saída para os arquivos HTML (padrão: 'docs/_build/html').",
    )
    build_cmd_parser.add_argument(
        "--clean",
        action="store_true",
        help="Limpa o diretório de saída antes de compilar.",
    )
    build_cmd_parser.add_argument(
        "--builder",
        default="html",
        help="Formato de saída do Sphinx (padrão: 'html').",
    )
    build_cmd_parser.add_argument(
        "-W",
        "--warnings-as-errors",
        action="store_true",
        help="Trata warnings do Sphinx como erros.",
    )
    build_cmd_parser.set_defaults(func=cmd_build)

    return parser


def main(argv: Optional[Sequence[str]] = None) -> int:
    """Main CLI entry point."""
    parser = build_parser()
    args = parser.parse_args(argv)

    if not hasattr(args, "func"):
        parser.print_help()
        return 0

    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
