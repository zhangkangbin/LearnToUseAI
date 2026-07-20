"""Build an offline HTML reading site from the AI learning Markdown series."""

from __future__ import annotations

import html
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTICLES = [
    ("基础篇", "普通人如何高效使用AI-基础篇.md", "普通人如何高效使用AI-基础篇.html"),
    ("进阶篇", "普通人如何高效使用AI-进阶篇.md", "普通人如何高效使用AI-进阶篇.html"),
    ("精通篇", "普通人如何高效使用AI-精通篇.md", "普通人如何高效使用AI-精通篇.html"),
]


STYLE = """
<style>
:root{--bg:#f7f8fb;--surface:#fff;--text:#202633;--muted:#667085;--line:#e4e7ec;--accent:#255fce;--code:#f1f4f8;--shadow:0 12px 35px rgba(25,35,55,.08)}
html[data-theme="dark"]{--bg:#111827;--surface:#1c2433;--text:#e6eaf0;--muted:#aeb7c5;--line:#344054;--accent:#86b4ff;--code:#151d29;--shadow:none}
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:var(--bg);color:var(--text);font:16px/1.85 ui-sans-serif,system-ui,"Microsoft YaHei",sans-serif}.progress{height:3px;background:transparent;position:fixed;z-index:10;inset:0 0 auto}.progress i{display:block;width:0;height:100%;background:var(--accent)}
.topbar{height:64px;display:flex;gap:12px;align-items:center;padding:0 max(20px,calc((100vw - 1240px)/2));border-bottom:1px solid var(--line);background:color-mix(in srgb,var(--bg) 90%,transparent);backdrop-filter:blur(12px);position:sticky;top:0;z-index:5}.brand{font-weight:750;color:var(--text);text-decoration:none;margin-right:auto}.topbar button{border:1px solid var(--line);background:var(--surface);color:var(--text);border-radius:8px;padding:6px 10px;cursor:pointer}.theme-switcher{display:flex;gap:4px}.theme-switcher button.active{background:var(--accent);border-color:var(--accent);color:white}
.layout{max-width:1240px;margin:0 auto;display:grid;grid-template-columns:260px minmax(0,1fr);gap:44px;padding:38px 28px 72px}.toc{position:sticky;top:92px;align-self:start;max-height:calc(100vh - 115px);overflow:auto;padding-right:14px}.toc h2{font-size:13px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);margin:0 0 10px}.toc a{display:block;color:var(--muted);text-decoration:none;font-size:14px;padding:5px 8px;border-left:2px solid transparent}.toc a[data-level="3"]{padding-left:20px;font-size:13px}.toc a.active{color:var(--accent);border-color:var(--accent);font-weight:700}
article{max-width:760px;min-width:0}article h1{font-size:2.25rem;line-height:1.3;margin:0 0 1.15rem;letter-spacing:-.03em}article h2{font-size:1.5rem;line-height:1.4;margin:3.2rem 0 1rem;padding-top:.25rem}article h3{font-size:1.13rem;margin:2rem 0 .7rem}article p,article li{overflow-wrap:anywhere}article a{color:var(--accent)}article blockquote{margin:1.4rem 0;padding:.7rem 1rem;border-left:4px solid var(--accent);background:var(--surface);color:var(--muted)}article pre{overflow:auto;background:var(--code);padding:16px;border-radius:10px;line-height:1.65}article code{font-family:ui-monospace,Consolas,monospace;background:var(--code);padding:.1em .3em;border-radius:4px}article pre code{padding:0;background:transparent}table{display:block;overflow:auto;border-collapse:collapse;max-width:100%}th,td{border:1px solid var(--line);padding:8px 12px;text-align:left}th{background:var(--code)}
.article-nav{display:flex;justify-content:space-between;gap:14px;border-top:1px solid var(--line);margin-top:54px;padding-top:24px}.article-nav a{background:var(--surface);box-shadow:var(--shadow);border-radius:10px;padding:12px 16px;text-decoration:none;max-width:48%}.article-nav a:last-child{text-align:right;margin-left:auto}.article-nav span{display:block;color:var(--muted);font-size:12px}.home{max-width:1000px;margin:0 auto;padding:70px 28px}.home h1{font-size:clamp(2rem,5vw,3.6rem);line-height:1.2;max-width:720px}.lead{color:var(--muted);font-size:1.13rem;max-width:680px}.sequence{color:var(--accent);font-weight:700;margin:2rem 0}.cards{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}.card{display:block;padding:24px;border-radius:14px;background:var(--surface);box-shadow:var(--shadow);color:var(--text);text-decoration:none;border:1px solid var(--line)}.card:hover{border-color:var(--accent);transform:translateY(-2px)}.card span{color:var(--accent);font-size:13px;font-weight:700}.card h2{margin:.45rem 0;font-size:1.35rem}.card p{color:var(--muted);margin:0}
@media(max-width:760px){.topbar{height:auto;min-height:58px;padding:8px 16px;flex-wrap:wrap}.theme-switcher{margin-left:auto}.layout{display:block;padding:26px 18px 56px}.toc{display:none;position:fixed;z-index:8;top:66px;left:12px;right:12px;max-height:70vh;padding:18px;background:var(--surface);border:1px solid var(--line);border-radius:12px;box-shadow:var(--shadow)}.toc.open{display:block}.cards{grid-template-columns:1fr}.home{padding:44px 20px}.article-nav{font-size:14px}}
</style>
"""


SCRIPT = """
<script>
(()=>{const root=document.documentElement,key='ai-learning-theme',buttons=[...document.querySelectorAll('[data-theme-choice]')];function setTheme(value){root.dataset.theme=value;localStorage.setItem(key,value);buttons.forEach(b=>b.classList.toggle('active',b.dataset.themeChoice===value));}setTheme(localStorage.getItem(key)||'system');buttons.forEach(b=>b.addEventListener('click',()=>setTheme(b.dataset.themeChoice)));
const bar=document.querySelector('#progressBar');if(bar)addEventListener('scroll',()=>{const max=document.documentElement.scrollHeight-innerHeight;bar.style.width=(max?scrollY/max*100:0)+'%';},{passive:true});
const toc=document.querySelector('.toc'),toggle=document.querySelector('#tocToggle');if(toggle&&toc)toggle.addEventListener('click',()=>toc.classList.toggle('open'));
const nav=document.querySelector('#tocNav'),headings=window.__headings||[];if(nav){nav.innerHTML='<h2>目录</h2>'+headings.filter(h=>h[0]>1).map(h=>`<a data-level="${h[0]}" href="#${h[2]}">${h[1]}</a>`).join('');const links=[...nav.querySelectorAll('a')],elements=headings.map(h=>document.getElementById(h[2])).filter(Boolean);new IntersectionObserver(entries=>{const visible=entries.filter(e=>e.isIntersecting).sort((a,b)=>a.boundingClientRect.top-b.boundingClientRect.top)[0];if(visible){links.forEach(a=>a.classList.toggle('active',a.hash==='#'+visible.target.id));}},{rootMargin:'-15% 0px -75% 0px'}).observe;elements.forEach(element=>new IntersectionObserver(entries=>{if(entries[0].isIntersecting){links.forEach(a=>a.classList.toggle('active',a.hash==='#'+element.id));}},{rootMargin:'-15% 0px -75% 0px'}).observe(element));}
})();
</script>
"""


def inline(text: str) -> str:
    value = html.escape(text, quote=False)
    value = re.sub(r"`([^`]+)`", r"<code>\1</code>", value)
    value = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", value)
    value = re.sub(r"\[([^]]+)\]\((https?://[^)]+)\)", r'<a href="\2" target="_blank" rel="noopener">\1</a>', value)
    value = re.sub(r"\[([^]]+)\]\(((?:\./|\.\./|/)[^)]+)\)", r'<a href="\2">\1</a>', value)
    return value


def slugify(title: str, seen: dict[str, int]) -> str:
    base = re.sub(r"[^\w\u4e00-\u9fff-]+", "-", title).strip("-") or "section"
    seen[base] = seen.get(base, 0) + 1
    return base if seen[base] == 1 else f"{base}-{seen[base]}"


def markdown_to_html(text: str) -> tuple[str, list[tuple[int, str, str]]]:
    lines, output, headings = text.splitlines(), [], []
    seen: dict[str, int] = {}
    index = 0
    while index < len(lines):
        line = lines[index]
        if not line.strip(): index += 1; continue
        match = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
        if match:
            level, title = len(match.group(1)), match.group(2)
            anchor = slugify(title, seen); headings.append((level, title, anchor))
            output.append(f'<h{level} id="{anchor}">{inline(title)}</h{level}>'); index += 1; continue
        if line.startswith("```"):
            language = line[3:].strip(); index += 1; code = []
            while index < len(lines) and not lines[index].startswith("```"): code.append(lines[index]); index += 1
            if index < len(lines): index += 1
            klass = f' class="language-{html.escape(language)}"' if language else ""
            output.append(f"<pre><code{klass}>{html.escape(chr(10).join(code))}</code></pre>"); continue
        if re.match(r"^[-*+]\s+", line) or re.match(r"^\d+\.\s+", line):
            ordered = bool(re.match(r"^\d+\.\s+", line)); tag = "ol" if ordered else "ul"; items = []
            pattern = r"^\d+\.\s+(.+)$" if ordered else r"^[-*+]\s+(.+)$"
            while index < len(lines) and (item := re.match(pattern, lines[index])): items.append(f"<li>{inline(item.group(1))}</li>"); index += 1
            output.append(f"<{tag}>" + "".join(items) + f"</{tag}>"); continue
        if line.startswith("> "):
            quote = []
            while index < len(lines) and lines[index].startswith("> "): quote.append(lines[index][2:]); index += 1
            output.append(f"<blockquote>{inline(' '.join(quote))}</blockquote>"); continue
        if line.startswith("|") and index + 1 < len(lines) and re.match(r"^\|?\s*:?-{3,}", lines[index + 1]):
            headers = [part.strip() for part in line.strip().strip("|").split("|")]; index += 2; rows = []
            while index < len(lines) and lines[index].startswith("|"):
                cells = [part.strip() for part in lines[index].strip().strip("|").split("|")]
                rows.append("<tr>" + "".join(f"<td>{inline(cell)}</td>" for cell in cells) + "</tr>"); index += 1
            output.append("<table><thead><tr>" + "".join(f"<th>{inline(cell)}</th>" for cell in headers) + "</tr></thead><tbody>" + "".join(rows) + "</tbody></table>"); continue
        paragraph = [line]; index += 1
        while index < len(lines) and lines[index].strip() and not re.match(r"^(#{1,6})\s+|^```|^[-*+]\s+|^\d+\.\s+|^> |^\|", lines[index]): paragraph.append(lines[index]); index += 1
        output.append(f"<p>{inline(' '.join(part.strip() for part in paragraph))}</p>")
    return "\n".join(output), headings


def render_article(title, body, headings, previous, next_article) -> str:
    nav = '<div class="article-nav">'
    if previous: nav += f'<a href="{previous["href"]}"><span>上一篇</span>{previous["label"]}</a>'
    if next_article: nav += f'<a href="{next_article["href"]}"><span>下一篇</span>{next_article["label"]}</a>'
    nav += "</div>"
    return f'''<!doctype html><html lang="zh-CN" data-theme="system"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{html.escape(title)}｜AI 学习系列</title>{STYLE}</head><body><div class="progress"><i id="progressBar"></i></div><header class="topbar"><a class="brand" href="index.html">AI 学习系列</a><button id="tocToggle" aria-label="打开目录">目录</button><div class="theme-switcher" aria-label="主题切换"><button data-theme-choice="light">浅色</button><button data-theme-choice="dark">深色</button><button data-theme-choice="system">系统</button></div></header><div class="layout"><aside class="toc"><nav id="tocNav"></nav></aside><main><article>{body}{nav}</article></main></div><script>window.__headings={json.dumps(headings, ensure_ascii=False)};</script>{SCRIPT}</body></html>'''


def render_index() -> str:
    cards = "".join(f'<a class="card" href="{href}"><span>第 {i + 1} 篇</span><h2>{label}</h2><p>从“{label}”开始阅读本系列。</p></a>' for i, (label, _, href) in enumerate(ARTICLES))
    return f'''<!doctype html><html lang="zh-CN" data-theme="system"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>AI 学习系列</title>{STYLE}</head><body><header class="topbar"><a class="brand" href="index.html">AI 学习系列</a><div class="theme-switcher" aria-label="主题切换"><button data-theme-choice="light">浅色</button><button data-theme-choice="dark">深色</button><button data-theme-choice="system">系统</button></div></header><main class="home"><p class="sequence">基础篇 → 进阶篇 → 精通篇</p><h1>普通人如何高效使用 AI</h1><p class="lead">一套从理解工具、建立工作流，到沉淀个人能力系统的离线阅读资料。</p><section class="cards">{cards}</section></main>{SCRIPT}</body></html>'''


def main() -> None:
    records = []
    for label, source_name, output_name in ARTICLES:
        source = ROOT / source_name
        if not source.exists(): raise FileNotFoundError(f"Missing source Markdown: {source}")
        body, headings = markdown_to_html(source.read_text(encoding="utf-8"))
        title = headings[0][1] if headings else label
        records.append((label, output_name, title, body, headings))
    for index, (_, output_name, title, body, headings) in enumerate(records):
        previous = {"label": records[index - 1][0], "href": records[index - 1][1]} if index else None
        next_article = {"label": records[index + 1][0], "href": records[index + 1][1]} if index + 1 < len(records) else None
        (ROOT / output_name).write_text(render_article(title, body, headings, previous, next_article), encoding="utf-8")
    (ROOT / "index.html").write_text(render_index(), encoding="utf-8")


if __name__ == "__main__":
    main()
