# AI 学习系列 HTML 阅读站 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 将三篇 AI 学习 Markdown 文章转换为带目录、主题切换、阅读进度和篇章导航的离线 HTML 阅读站。

**Architecture:** 新增零依赖 Python 生成器，读取三份 UTF-8 Markdown 并输出入口页和三份文章页。生成器内置轻量 Markdown 转换、目录锚点、CSS 和 JavaScript 模板；单元测试覆盖转换和产物结构。

**Tech Stack:** Python 3 标准库、HTML5、CSS、原生 JavaScript、unittest。

---

### Task 1: 添加生成器转换测试

**Files:**

- Create: `tools/test_build_ai_learning_html.py`
- Test: `tools/test_build_ai_learning_html.py`

- [ ] **Step 1: 写入失败测试**

```python
import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("builder", ROOT / "tools" / "build_ai_learning_html.py")
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)

class MarkdownConversionTests(unittest.TestCase):
    def test_markdown_to_html_builds_heading_anchor_and_list(self):
        html, headings = builder.markdown_to_html("# 标题\\n\\n- 第一项\\n- 第二项")
        self.assertIn('<h1 id="标题">标题</h1>', html)
        self.assertIn('<ul><li>第一项</li><li>第二项</li></ul>', html)
        self.assertEqual(headings, [(1, "标题", "标题")])

    def test_render_article_includes_reader_controls(self):
        html = builder.render_article("测试文章", "<p>正文</p>", [(2, "章节", "章节")], None, None)
        self.assertIn('data-theme="system"', html)
        self.assertIn('aria-label="主题切换"', html)
        self.assertIn('class="toc"', html)
        self.assertIn('class="progress"', html)
```

- [ ] **Step 2: 运行测试确认失败**

Run: `python -m unittest tools/test_build_ai_learning_html.py -v`

Expected: FAIL，提示 `tools/build_ai_learning_html.py` 不存在。

- [ ] **Step 3: 提交测试基线**

Run: `git add -- tools/test_build_ai_learning_html.py; git commit -m "test: cover AI learning HTML conversion"`

### Task 2: 实现离线 HTML 生成器

**Files:**

- Create: `tools/build_ai_learning_html.py`
- Modify: `tools/test_build_ai_learning_html.py`

- [ ] **Step 1: 实现转换和渲染 API**

在生成器定义 `markdown_to_html(text: str) -> tuple[str, list[tuple[int, str, str]]]` 与 `render_article(title, body, headings, previous, next_article) -> str`。按行处理 ATX 标题、围栏代码块、无序/有序列表、引用、表格、段落及链接、加粗、行内代码；标题 ID 使用 `re.sub(r"[^\\w\\u4e00-\\u9fff-]+", "-", title).strip("-")`，重复 ID 追加序号。

渲染的文章模板必须有以下结构：

```html
<html lang="zh-CN" data-theme="system">
<div class="progress"><i id="progressBar"></i></div>
<header class="topbar"><a href="index.html">AI 学习系列</a><button id="tocToggle" aria-label="打开目录">目录</button><div class="theme-switcher" aria-label="主题切换"><button data-theme-choice="light">浅色</button><button data-theme-choice="dark">深色</button><button data-theme-choice="system">系统</button></div></header>
<aside class="toc"><nav id="tocNav"></nav></aside>
<main><article><!-- converted body --></article></main>
```

内嵌 CSS 需定义浅色/深色变量、正文最大宽度 760px、代码和表格横向滚动、`max-width: 760px` 的目录抽屉。内嵌 JS 用 headings JSON 创建目录、以 `IntersectionObserver` 高亮、以 scroll 更新 `#progressBar`，并把主题选择保存到 `localStorage` 的 `ai-learning-theme`。

- [ ] **Step 2: 实现文件读取与站点入口**

在 `main()` 使用如下清单读取仓库根目录；缺少源文件时抛出 `FileNotFoundError`。提取一级标题为文章页标题，按数组顺序传入上一篇、下一篇。所有页面写为 UTF-8：

```python
ARTICLES = [
    ("基础篇", "普通人如何高效使用AI-基础篇.md", "普通人如何高效使用AI-基础篇.html"),
    ("进阶篇", "普通人如何高效使用AI-进阶篇.md", "普通人如何高效使用AI-进阶篇.html"),
    ("精通篇", "普通人如何高效使用AI-精通篇.md", "普通人如何高效使用AI-精通篇.html"),
]
```

`index.html` 使用三张文章卡片连接这三个输出文件，并明确展示“基础篇 → 进阶篇 → 精通篇”的阅读顺序。

- [ ] **Step 3: 运行单元测试**

Run: `python -m unittest tools/test_build_ai_learning_html.py -v`

Expected: PASS，2 tests。

- [ ] **Step 4: 生成页面**

Run: `python tools/build_ai_learning_html.py`

Expected: 退出码 0，创建 `index.html` 和三份文章 HTML。

- [ ] **Step 5: 提交生成器和产物**

Run: `git add -- tools/build_ai_learning_html.py index.html '普通人如何高效使用AI-基础篇.html' '普通人如何高效使用AI-进阶篇.html' '普通人如何高效使用AI-精通篇.html'; git commit -m "feat: publish offline AI learning HTML reader"`

### Task 3: 验证生成页面

**Files:**

- Modify: `tools/test_build_ai_learning_html.py`
- Verify: `index.html`
- Verify: `普通人如何高效使用AI-基础篇.html`
- Verify: `普通人如何高效使用AI-进阶篇.html`
- Verify: `普通人如何高效使用AI-精通篇.html`

- [ ] **Step 1: 添加生成产物断言**

```python
class GeneratedSiteTests(unittest.TestCase):
    def test_generated_pages_include_required_reader_features(self):
        expected = ["index.html", "普通人如何高效使用AI-基础篇.html", "普通人如何高效使用AI-进阶篇.html", "普通人如何高效使用AI-精通篇.html"]
        for name in expected:
            page = (ROOT / name).read_text(encoding="utf-8")
            self.assertIn('<meta charset="utf-8">', page)
            self.assertIn('data-theme', page)
        article = (ROOT / expected[1]).read_text(encoding="utf-8")
        self.assertIn('class="toc"', article)
        self.assertIn('id="progressBar"', article)
        self.assertIn('普通人如何高效使用 AI', article)
```

- [ ] **Step 2: 生成并执行完整测试**

Run: `python tools/build_ai_learning_html.py; python -m unittest tools/test_build_ai_learning_html.py -v`

Expected: PASS，3 tests；四个 HTML 均可用 UTF-8 读取。

- [ ] **Step 3: 静态检查交互和链接**

Run: `rg -n '普通人如何高效使用AI-(基础|进阶|精通)篇\.html|ai-learning-theme|IntersectionObserver|progressBar' index.html '普通人如何高效使用AI-基础篇.html' '普通人如何高效使用AI-进阶篇.html' '普通人如何高效使用AI-精通篇.html'`

Expected: 入口页含三个篇章链接，文章页含主题、目录高亮和进度条代码。

- [ ] **Step 4: 提交验证测试**

Run: `git add -- tools/test_build_ai_learning_html.py; git commit -m "test: verify generated AI learning reader pages"`
