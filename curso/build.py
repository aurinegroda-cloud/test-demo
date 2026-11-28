"""Genera curso.html (página única navegable) a partir de los capítulos en Markdown.

Uso: python3 curso/build.py   (requiere: pip install markdown)
"""
import html
import json
import re
from pathlib import Path

import markdown
from markdown.extensions.toc import slugify

HERE = Path(__file__).parent
CHAPTERS = [
    ("ruta", "00-ruta.md", "Tu ruta"),
    ("nichos", "01-nichos.md", "Nichos"),
    ("youtube", "02-youtube.md", "YouTube"),
    ("tiktok", "03-tiktok.md", "TikTok"),
    ("instagram", "04-instagram.md", "Instagram"),
    ("hotmart", "05-hotmart.md", "Hotmart"),
    ("shopify", "06-shopify.md", "Shopify"),
    ("herramientas", "07-herramientas.md", "Herramientas"),
]


def fix_indent(text: str) -> str:
    """Python-Markdown necesita 4 espacios por nivel en listas anidadas."""
    out = []
    for line in text.splitlines():
        m = re.match(r"^( +)([-*+]|\d+\.) ", line)
        if m and len(m.group(1)) % 4:
            level = max(1, round(len(m.group(1)) / 2))
            line = " " * (4 * level) + line[len(m.group(1)):]
        out.append(line)
    return "\n".join(out)


def render(slug: str, text: str):
    md = markdown.Markdown(
        extensions=["tables", "fenced_code", "toc", "sane_lists"],
        extension_configs={"toc": {"slugify": lambda v, s: f"{slug}-{slugify(v, s)}"[:80], "toc_depth": "2-3"}},
    )
    body = md.convert(fix_indent(text))
    # El primer h1 se muestra en la cabecera del capítulo
    title_m = re.search(r"<h1[^>]*>(.*?)</h1>", body, re.S)
    title = title_m.group(1) if title_m else slug
    body = re.sub(r"<h1[^>]*>.*?</h1>", "", body, count=1, flags=re.S)
    body = body.replace("<table>", '<div class="tw"><table>').replace("</table>", "</table></div>")
    body = re.sub(r'(?<![">=])(https?://[^\s<>"]+[^\s<>".,;:)])', r'<a href="\1">\1</a>', body)
    body = re.sub(r'<a href="(https?://[^"]+)"', r'<a href="\1" target="_blank" rel="noopener"', body)
    n = 0

    def task(m):
        nonlocal n
        n += 1
        tid = f"t-{slug}-{n}"
        return (f'<div class="task"><input type="checkbox" id="{tid}" aria-label="Marcar tarea como hecha">'
                f'<div class="task-body"><span class="task-k">Tarea</span><p>{m.group(1).strip()}</div></div>')

    body = re.sub(r"<blockquote>\s*<p><strong>Tarea:?</strong>:?(.*?)</blockquote>", task, body, flags=re.S)
    toc = [{"id": t["id"], "name": html.unescape(t["name"])} for t in md.toc_tokens if t["level"] == 2]
    words = len(re.sub(r"<[^>]+>", " ", body).split())
    return title, body, toc, n, words


def main():
    sections, nav = [], []
    total_tasks = 0
    for i, (slug, fname, label) in enumerate(CHAPTERS):
        p = HERE / fname
        if not p.exists():
            print("falta", fname)
            continue
        title, body, toc, ntasks, words = render(slug, p.read_text(encoding="utf-8"))
        total_tasks += ntasks
        mins = max(3, round(words / 200))
        sections.append(
            f'<section class="chapter" id="{slug}" data-label="{label}" hidden>'
            f'<header class="ch-head"><p class="eyebrow">Capítulo {i} · {mins} min de lectura · '
            f'<span class="ch-prog" data-ch="{slug}">{ntasks} tareas</span></p><h1>{title}</h1></header>'
            f'<div class="prose">{body}</div><nav class="pager" data-i="{i}"></nav></section>'
        )
        nav.append({"slug": slug, "label": label, "n": i, "toc": toc, "tasks": ntasks})
    tpl = (HERE / "template.html").read_text(encoding="utf-8")
    out = (tpl.replace("{{SECTIONS}}", "\n".join(sections))
              .replace("{{NAV}}", json.dumps(nav, ensure_ascii=False))
              .replace("{{TOTAL_TASKS}}", str(total_tasks))
              .replace("{{N_CH}}", str(len(nav))))
    (HERE / "curso.html").write_text(out, encoding="utf-8")
    print(f"curso.html: {len(nav)} capítulos, {total_tasks} tareas, {len(out)//1024} KB")


if __name__ == "__main__":
    main()
