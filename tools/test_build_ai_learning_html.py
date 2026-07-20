import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "tools" / "build_ai_learning_html.py"


def load_builder():
    if not MODULE_PATH.exists():
        raise AssertionError(f"Missing generator: {MODULE_PATH}")

    spec = importlib.util.spec_from_file_location("builder", MODULE_PATH)
    builder = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(builder)
    return builder


class MarkdownConversionTests(unittest.TestCase):
    def test_markdown_to_html_builds_heading_anchor_and_list(self):
        builder = load_builder()
        html, headings = builder.markdown_to_html(
            "# 标题\n\n- 第一项\n- 第二项\n\n[学习路线](./advanced-ai-system/README.md)"
        )

        self.assertIn('<h1 id="标题">标题</h1>', html)
        self.assertIn('<ul><li>第一项</li><li>第二项</li></ul>', html)
        self.assertIn('<a href="./advanced-ai-system/README.md">学习路线</a>', html)
        self.assertEqual(headings, [(1, "标题", "标题")])

    def test_render_article_includes_reader_controls(self):
        builder = load_builder()
        html = builder.render_article("测试文章", "<p>正文</p>", [(2, "章节", "章节")], None, None)

        self.assertIn('data-theme="system"', html)
        self.assertIn('aria-label="主题切换"', html)
        self.assertIn('class="toc"', html)
        self.assertIn('class="progress"', html)


class GeneratedSiteTests(unittest.TestCase):
    def test_generated_pages_include_required_reader_features(self):
        expected = [
            "index.html",
            "普通人如何高效使用AI-基础篇.html",
            "普通人如何高效使用AI-进阶篇.html",
            "普通人如何高效使用AI-精通篇.html",
        ]
        for name in expected:
            path = ROOT / name
            self.assertTrue(path.exists(), f"Missing generated page: {path}")
            page = path.read_text(encoding="utf-8")
            self.assertIn('<meta charset="utf-8">', page)
            self.assertIn('data-theme', page)

        article = (ROOT / expected[1]).read_text(encoding="utf-8")
        self.assertIn('class="toc"', article)
        self.assertIn('id="progressBar"', article)
        self.assertIn('普通人如何高效使用 AI', article)


if __name__ == "__main__":
    unittest.main()
