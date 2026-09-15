#!/usr/bin/env python3
"""Genera el README del perfil desde los topics `area-*` de los repositorios.

La regla que hace posible el índice: cada repositorio lleva EXACTAMENTE UN topic
`area-*`. Es la «carpeta». El resto de topics es el stack. La descripción del
repo es el «qué es». Nada de eso se escribe aquí: se lee de GitHub.

Lo que sí se escribe a mano está en `perfil.toml`: cabecera, destacados y el
orden, emoji e introducción de cada área.

    python3 scripts/generar_readme.py            # reescribe README.md
    python3 scripts/generar_readme.py --check    # 0 si README.md concuerda, 1 si no

Solo entran los repositorios PÚBLICOS y no archivados: el README es público.
Necesita `gh` autenticado (en Actions, GITHUB_TOKEN basta para listar los públicos).
"""
import json
import pathlib
import subprocess
import sys
import tomllib
from urllib.parse import quote

RAIZ = pathlib.Path(__file__).resolve().parent.parent
CONFIG = RAIZ / "perfil.toml"
README = RAIZ / "README.md"
MAX_STACK = 3


def repos(usuario: str) -> list[dict]:
    salida = subprocess.run(
        ["gh", "repo", "list", usuario, "--limit", "300", "--json",
         "name,description,repositoryTopics,visibility,isArchived,isFork,url"],
        check=True, capture_output=True, text=True,
    ).stdout
    return json.loads(salida)


def area_de(repo: dict) -> str | None:
    """El único topic `area-*`. Más de uno o ninguno es un error del diseño, no del script."""
    areas = sorted(t["name"][5:] for t in (repo.get("repositoryTopics") or []) if t["name"].startswith("area-"))
    if len(areas) > 1:
        raise SystemExit(f"✗ {repo['name']}: {len(areas)} topics area-* ({', '.join(areas)}). Tiene que ser uno.")
    return areas[0] if areas else None


def stack_de(repo: dict, ocultos: set[str]) -> str:
    topics = sorted(t["name"] for t in (repo.get("repositoryTopics") or [])
                    if not t["name"].startswith("area-") and t["name"] not in ocultos)
    return " · ".join(f"`{t}`" for t in topics[:MAX_STACK])


def fila(repo: dict, ocultos: set[str]) -> str:
    fork = " *(fork)*" if repo.get("isFork") else ""
    return f"| [{repo['name']}]({repo['url']}){fork} | {stack_de(repo, ocultos)} | {repo.get('description') or ''} |"


def generar(cfg: dict, todos: list[dict]) -> str:
    usuario = cfg["usuario"]
    ocultos = set(cfg.get("topics_ocultos", []))
    publicos = [r for r in todos if r["visibility"] == "PUBLIC" and not r["isArchived"] and r["name"] != usuario]
    por_area: dict[str, list[dict]] = {}
    sin_area = []
    for r in publicos:
        a = area_de(r)
        if a is None:
            sin_area.append(r["name"])
            continue
        por_area.setdefault(a, []).append(r)
    for nombre in sin_area:
        print(f"! {nombre}: sin topic area-*, no entra en el índice", file=sys.stderr)

    # Orden: el del toml; las áreas que no estén allí, al final por nombre.
    orden = list(cfg["areas"].keys()) + sorted(a for a in por_area if a not in cfg["areas"])
    orden = [a for a in orden if a in por_area]

    def meta(a: str) -> dict:
        return cfg["areas"].get(a, {"emoji": "📁", "nombre": a})

    por_nombre = {r["name"]: r for r in publicos}
    out = [cfg["cabecera"].strip(), "", "---", "", "### Destacados", ""]
    for n in cfg.get("destacados", []):
        r = por_nombre.get(n)
        if r is None:
            raise SystemExit(f"✗ destacado {n!r} no es un repo público")
        out.append(f"- **[{n}]({r['url']})** — {r.get('description') or ''}")

    out += ["", "### Repositorios por área", "", "Cada área es un topic filtrable y una lista navegable.", "",
            "| Área | Repos | Explorar |", "|---|---|---|"]
    for a in orden:
        m = meta(a)
        lista = f"https://github.com/stars/{usuario}/lists/{a}"
        topic = f"https://github.com/search?q={quote(f'user:{usuario} topic:area-{a}')}&type=repositories"
        out.append(f"| {m['emoji']} **{m['nombre']}** | {len(por_area[a])} | [lista]({lista}) · [topic]({topic}) |")

    for a in orden:
        m = meta(a)
        rs = sorted(por_area[a], key=lambda r: r["name"].lower())
        out += ["", "<details>", f"<summary><b>{m['emoji']} {m['nombre']}</b> — {len(rs)} repos</summary>", ""]
        if m.get("intro"):
            out += [m["intro"].strip(), ""]
        out += ["| Repo | Stack | Qué es |", "|---|---|---|"]
        out += [fila(r, ocultos) for r in rs]
        if m.get("nota"):
            out += ["", m["nota"].strip()]
        out += ["", "</details>"]

    out += ["", "<sub>Índice generado por <code>scripts/generar_readme.py</code> desde los topics "
            "<code>area-*</code> de cada repo. No se edita a mano.</sub>", ""]
    return "\n".join(out)


def main() -> int:
    cfg = tomllib.loads(CONFIG.read_text(encoding="utf-8"))
    nuevo = generar(cfg, repos(cfg["usuario"]))
    if "--check" in sys.argv:
        actual = README.read_text(encoding="utf-8") if README.exists() else ""
        if actual == nuevo:
            print("✓ README.md concuerda con los topics")
            return 0
        print("✗ README.md no concuerda: ejecuta scripts/generar_readme.py y commitea", file=sys.stderr)
        return 1
    README.write_text(nuevo, encoding="utf-8")
    print(f"✓ README.md regenerado ({nuevo.count(chr(10))} líneas)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
