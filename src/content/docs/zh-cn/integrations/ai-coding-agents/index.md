---
title: AI 代理（MCP）
description: 通过模型上下文协议（MCP）服务器，将 Claude、Cursor、GitHub Copilot、Gemini 及其他 AI 代理连接到您的 PlaidCloud 租户。
sidebar:
  label: AI 代理（MCP）
  order: 13
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/integrations/ai-coding-agents/index.md
---

PlaidCloud 在每个工作区的 `/mcp` 路径上提供一个精心设计的[模型上下文协议](https://modelcontextprotocol.io)（MCP）服务器。AI 代理连接它的方式与连接任何其他 MCP 服务器相同，然后即可调用各种工具来读取项目、运行工作流、查询表、管理维度等。

本节页面介绍服务器提供的功能、身份验证方式，以及最常见 AI 客户端的分步设置。有关其背后的架构，包括每个 AI 请求所经过的受治理路径、检索的工作方式以及如何运行自己的模型，请参阅 [AI 与 LLM 架构](/zh-cn/integrations/ai-architecture/)。

## PlaidCloud 的 AI 分析有何不同

- **[值得信赖的答案](./honest-answers/)**：每个答案都附带置信度信号和通俗易懂的注意事项，PlaidCloud 绝不会编造数字。正因为如此诚实，您才能直接依据 AI 的答案采取行动，而无需手动重新核对。
- **[追溯分摊](./tracing-allocations/)**：用通俗语言询问分摊结果为何发生变化、由什么构成，以及假设的改动会带来什么影响。
- **[分析路径](./analysis-paths/)**：为关键表设置易记的名称和默认值，这样您只需直接提问“上季度这个数字为什么上升了？”
- **[构建仪表板](./build-dashboards/)**：通过同一个 PlaidCloud 连接，基于已发布的表和视图请求生成图表和仪表板。
- **[指标定义](./metric-definitions/)**：一次性约定某个业务数字的计算方式，使所有用到它的答案都按相同方式计算。

## 连接您的助手

最快的方式是使用 PlaidCloud 自身页眉工具栏中的 **连接您的 AI** 按钮：选择您的客户端并按照显示的步骤操作，其中已包含 MCP 服务器 URL。

- [入门](./getting-started/)：MCP 服务器提供的功能以及如何进行身份验证。
- [Microsoft 365 Copilot](/zh-cn/integrations/microsoft-365-copilot/)：在 Teams 和 Outlook 中为整个团队提供 PlaidCloud。
- 各客户端的设置：[Claude Code](./claude-code/)、[Claude Desktop](./claude-desktop/)、[Cursor](./cursor/)、[GitHub Copilot](./copilot/)、[Gemini](./gemini/)、[ChatGPT](./chatgpt/)、[Grok](./grok/)。
