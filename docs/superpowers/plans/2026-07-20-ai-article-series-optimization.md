# AI 使用指南系列优化实施计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 将基础、进阶、精通三篇 AI 使用指南改造成递进清晰、可练习、可核查的文章系列。

**Architecture:** 保留原有文章正文，以增补和局部改写的方式建立统一导航、模板和案例规范。基础篇强调单任务协作，进阶篇强调端到端工作流，精通篇强调质量与治理体系。

**Tech Stack:** UTF-8 Markdown、PowerShell、ripgrep。

---

### Task 1: 建立三篇文章的系列导航

**Files:**
- Modify: `E:\KangWorkInfo\LearnToUseAI\普通人如何高效使用AI-基础篇.md:3`
- Modify: `E:\KangWorkInfo\LearnToUseAI\普通人如何高效使用AI-进阶篇.md:3`
- Modify: `E:\KangWorkInfo\LearnToUseAI\普通人如何高效使用AI-精通篇.md:3`

- [ ] 增加“适合谁、前置能力、完成后可交付成果、下一篇”的阅读导航和目录链接。
- [ ] 使用 `rg -n '^## ' -g '*.md'` 验证三篇的顶级章节可发现。

### Task 2: 强化基础篇的可执行性与安全边界

**Files:**
- Modify: `E:\KangWorkInfo\LearnToUseAI\普通人如何高效使用AI-基础篇.md:111`
- Modify: `E:\KangWorkInfo\LearnToUseAI\普通人如何高效使用AI-基础篇.md:615`

- [ ] 将提示词框架扩充为任务、材料、受众、格式、约束、验收与核查。
- [ ] 新增端到端案例和模板使用说明。
- [ ] 增加专业高风险领域、隐私和工具设置的操作性检查清单。

### Task 3: 以工作流重构进阶篇主线

**Files:**
- Modify: `E:\KangWorkInfo\LearnToUseAI\普通人如何高效使用AI-进阶篇.md:15`
- Modify: `E:\KangWorkInfo\LearnToUseAI\普通人如何高效使用AI-进阶篇.md:249`

- [ ] 在文章前部定义统一的七步工作流和每步产出。
- [ ] 增加“输入—追问—审核—交付—沉淀”的端到端案例与验收标准。
- [ ] 添加工作流复盘模板，避免只停留在抽象原则。

### Task 4: 提升精通篇的质量与协作系统内容

**Files:**
- Modify: `E:\KangWorkInfo\LearnToUseAI\普通人如何高效使用AI-精通篇.md:67`
- Modify: `E:\KangWorkInfo\LearnToUseAI\普通人如何高效使用AI-精通篇.md:529`
- Modify: `E:\KangWorkInfo\LearnToUseAI\普通人如何高效使用AI-精通篇.md:564`

- [ ] 增加质量门、版本与责任边界、团队协作和使用指标的可操作说明。
- [ ] 将隐私章节扩展为数据分级、脱敏、授权与工具设置检查。
- [ ] 添加系统级端到端案例及量化评估表。

### Task 5: 结构与覆盖验证

**Files:**
- Verify: `E:\KangWorkInfo\LearnToUseAI\普通人如何高效使用AI-基础篇.md`
- Verify: `E:\KangWorkInfo\LearnToUseAI\普通人如何高效使用AI-进阶篇.md`
- Verify: `E:\KangWorkInfo\LearnToUseAI\普通人如何高效使用AI-精通篇.md`

- [ ] 用 PowerShell 检查三篇文件为 UTF-8、所有代码围栏成对出现、标题层级存在。
- [ ] 用 `rg` 核查每篇均含导航、目录、案例、验收、安全或核查、下一步行动。
- [ ] 人工复读新增部分，确认各篇定位没有混淆且无遗留占位符。
