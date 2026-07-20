# Reading and Learning Navigation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create a root-level Chinese navigation article that provides both a progressive curriculum and goal-oriented shortcut routes through every learning series in the repository.

**Architecture:** Keep the navigation as one reader-facing Markdown document at the repository root, with links to the existing articles as the source of truth. Organize it into a five-stage main path, five shortcut paths, four advanced-topic phases, and a reusable study-and-practice method.

**Tech Stack:** Markdown, Mermaid, PowerShell link validation, Git

---

### Task 1: Create the root navigation article

**Files:**
- Create: `阅读与学习导航.md`

- [x] **Step 1: Add the progressive learning path**

Create the article with the exact stage order below and link every stage to its existing source material:

```text
基础篇 → 进阶篇 → 精通篇 → Skill/MCP/函数调用专题 → 高级 AI 系统
```

- [x] **Step 2: Add completion guidance for every stage**

For each stage, include these three fields:

```text
学习目标 / 推荐输出 / 完成标准
```

- [x] **Step 3: Add five shortcut routes**

Add exact linked reading sequences for these audiences:

```text
职场提效 / AI 自动化开发 / RAG 知识库 / 生产可靠性与安全 / 多智能体架构
```

- [x] **Step 4: Add the advanced-system phase index**

Group and link all 28 advanced articles in these ranges:

```text
01—05 核心基础
06—09 可信知识与记忆
10—17 可靠性与安全
18—28 复杂智能体系统
```

- [x] **Step 5: Add the practice method and starting guide**

Explain the repeatable cycle “理解概念 → 阅读图示 → 跑通案例 → 完成练习 → 复盘记录”, use a project-weekly-report assistant as the running project, list common mistakes, and end with clear starting points for different readers.

### Task 2: Validate the navigation

**Files:**
- Test: `阅读与学习导航.md`

- [x] **Step 1: Verify all relative links resolve**

Run a PowerShell script that extracts Markdown links from `阅读与学习导航.md`, ignores web URLs and anchors, resolves each path from the file directory, and fails if any target does not exist.

Expected: `导航链接检查通过` and zero missing paths.

- [x] **Step 2: Verify Markdown fences**

Count lines beginning with three backticks in `阅读与学习导航.md`.

Expected: an even number of fences.

- [x] **Step 3: Verify required coverage**

Search the article for the three root series, the four AI capability topics, all advanced ranges from 01 through 28, five shortcut-route headings, and at least one `mermaid` fence.

Expected: every required section is present.

- [x] **Step 4: Review the final diff**

Run:

```powershell
git diff --check
git status -sb
git diff --stat
```

Expected: no whitespace errors; only the design, plan, and navigation files are new on `agent/reading-learning-navigation`.
