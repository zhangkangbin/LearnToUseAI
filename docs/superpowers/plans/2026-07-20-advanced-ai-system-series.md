# Advanced AI System Article Series Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 按既定目录生成 28 篇独立、详细、图文结合的中文高级 AI 系统文章。

**Architecture:** 在 `advanced-ai-system/` 下建立总目录和 28 个编号文件。每篇统一包含概念、架构图、实例、实践步骤、常见错误、安全边界、练习与参考资料，并通过上一篇/下一篇链接形成学习路径。

**Tech Stack:** UTF-8 Markdown、Mermaid、JSON/TypeScript/Python 示例、官方技术文档链接。

---

### Task 1: 建立总目录与统一规范

**Files:**
- Create: `advanced-ai-system/README.md`

- [ ] 写出四阶段学习路线、28 篇文章链接和统一阅读说明。
- [ ] 检查目录中每个链接都对应一个编号文件。

### Task 2: 核心基础（01-05）

**Files:**
- Create: `advanced-ai-system/01-上下文工程.md`
- Create: `advanced-ai-system/02-结构化输出与JSON模式.md`
- Create: `advanced-ai-system/03-工具设计.md`
- Create: `advanced-ai-system/04-智能体循环.md`
- Create: `advanced-ai-system/05-状态管理.md`

- [ ] 每篇加入至少一幅 Mermaid 图、一个贯穿案例和一个练习。
- [ ] 检查代码围栏、术语和官方参考链接。

### Task 3: 可信知识与记忆（06-09）

**Files:**
- Create: `advanced-ai-system/06-检索增强生成.md`
- Create: `advanced-ai-system/07-知识库更新机制.md`
- Create: `advanced-ai-system/08-记忆系统.md`
- Create: `advanced-ai-system/09-上下文压缩与摘要.md`

- [ ] 覆盖检索、版本、权限、记忆边界和长任务压缩。
- [ ] 检查每篇均含失败模式和验证方法。

### Task 4: 可靠性与安全（10-17）

**Files:**
- Create: `advanced-ai-system/10-评估系统.md`
- Create: `advanced-ai-system/11-链路追踪与可观测性.md`
- Create: `advanced-ai-system/12-人工参与机制.md`
- Create: `advanced-ai-system/13-安全护栏.md`
- Create: `advanced-ai-system/14-提示词注入防护.md`
- Create: `advanced-ai-system/15-权限审计与密钥管理.md`
- Create: `advanced-ai-system/16-重试超时幂等与补偿.md`
- Create: `advanced-ai-system/17-成本与性能优化.md`

- [ ] 每篇给出生产检查清单和可度量验收项。
- [ ] 检查安全内容不把模型自检描述为确定性保证。

### Task 5: 复杂智能体系统（18-28）

**Files:**
- Create: `advanced-ai-system/18-工作流与智能体.md`
- Create: `advanced-ai-system/19-多智能体与任务交接.md`
- Create: `advanced-ai-system/20-计划反思与批判机制.md`
- Create: `advanced-ai-system/21-计算机操作与浏览器自动化.md`
- Create: `advanced-ai-system/22-后台任务与长时间运行.md`
- Create: `advanced-ai-system/23-插件与应用封装.md`
- Create: `advanced-ai-system/24-钩子与策略执行.md`
- Create: `advanced-ai-system/25-多模态人工智能.md`
- Create: `advanced-ai-system/26-实时智能体.md`
- Create: `advanced-ai-system/27-微调蒸馏与模型适配.md`
- Create: `advanced-ai-system/28-人工智能治理与红队测试.md`

- [ ] 覆盖复杂编排、自动化、多模态、模型适配和治理。
- [ ] 检查每篇都明确适用与不适用场景。

### Task 6: 系列入口与完整验证

**Files:**
- Modify: `普通人如何高效使用AI-精通篇.md`
- Verify: `advanced-ai-system/*.md`

- [ ] 在精通版加入高级系列入口。
- [ ] 验证 28 个编号文件全部存在、标题和目录一致。
- [ ] 验证所有代码围栏成对、Mermaid 图存在、本地链接有效、无占位符。
