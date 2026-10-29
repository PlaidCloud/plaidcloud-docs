---
title: AI 助手
description: 使用 PlaidCloud 内置的 AI 助手，以自然语言提问、生成表达式并操作您的项目。
sidebar:
  label: AI 助手
  order: 14
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/ai-assistant/index.md
---

PlaidCloud AI 助手是应用内的聊天体验，可用自然语言就数据提问、生成工作流表达式并执行操作。它有别于 [AI 代理 (MCP)](/zh-cn/integrations/ai-coding-agents/) 部分，后者介绍如何将外部 AI 客户端连接到您的租户。

如需了解其底层原理，包括由哪个模型作答、检索如何为答案提供依据，以及由什么来管控访问，请阅读 [AI 和 LLM 架构](/zh-cn/integrations/ai-architecture/)。

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 700 210" role="img" aria-label="您用自然语言向 AI 助手提问。在项目范围内，助手检索项目的数据和元数据作为回答的依据，然后返回答案。对话会被保留，每个对话都与其开始时所在的项目相关联；在对话归属于项目之前创建的旧对话除外，它们会显示在每个项目的历史记录中。" style="width:100%;max-width:700px;height:auto;">
  <defs><marker id="ai-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <rect x="14" y="78" width="140" height="46" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="84" y="100" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">您的问题</text>
  <text x="84" y="116" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">自然语言</text>
  <path d="M154 101 L190 101" stroke="var(--sl-color-gray-3)" stroke-width="1.8" fill="none" marker-end="url(#ai-arrow)" />
  <rect x="192" y="44" width="184" height="150" rx="12" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" stroke-dasharray="6 4" />
  <text x="204" y="38" font-size="12" font-weight="700" fill="var(--sl-color-accent)">项目范围</text>
  <rect x="214" y="66" width="140" height="52" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-accent)" stroke-width="1.6" />
  <text x="284" y="96" text-anchor="middle" font-size="12" font-weight="700" fill="var(--sl-color-text)">AI 助手</text>
  <rect x="214" y="140" width="140" height="40" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="284" y="158" text-anchor="middle" font-size="10" fill="var(--sl-color-text)">项目数据 + 元数据</text>
  <text x="284" y="172" text-anchor="middle" font-size="9" fill="var(--sl-color-gray-3)">表 · 工作流 · 维度</text>
  <path d="M284 140 L284 120" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#ai-arrow)" />
  <text x="360" y="134" font-size="9" fill="var(--sl-color-gray-3)">检索</text>
  <path d="M376 92 L520 92" stroke="var(--sl-color-gray-3)" stroke-width="1.8" fill="none" marker-end="url(#ai-arrow)" />
  <rect x="522" y="66" width="150" height="52" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="597" y="90" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">有依据的答案</text>
  <text x="597" y="107" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">引用您的数据</text>
  <text x="284" y="205" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">对话会被保留</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">您用自然语言提问；在项目范围内，助手检索您的数据和元数据作为回答的依据。对话会被保留，每个对话都与其开始时所在的项目相关联；在对话归属于项目之前创建的旧对话会显示在每个项目的历史记录中，并标记为（无项目）。完整机制请参阅 <a href="/zh-cn/integrations/ai-architecture/">AI 和 LLM 架构</a>。</figcaption>
</figure>

AI 辅助也会直接出现在某些工作流步骤中，例如根据自然语言描述[生成 SQL 提取步骤的查询](/zh-cn/guides/ai-assistant/generate-sql-extract/)。
