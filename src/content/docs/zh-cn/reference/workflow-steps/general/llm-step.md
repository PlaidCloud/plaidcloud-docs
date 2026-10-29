---
title: LLM 步骤
description: 对 LLM 运行提示词，并授予对项目数据的限定读取和/或写入权限，模型通过 MCP 服务器直接写回结果。
sidebar:
  order: 5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/llm-step.md
---

## 说明

**LLM 步骤**将提示词发送给大型语言模型。使用 Anthropic LLM 连接时，模型可限定访问您绑定的项目表、维度和文档——每个对象可设为**读取**、**写入**或两者兼有——并将结果直接写入启用了写入的绑定。写入绑定就是该步骤的输出；没有单独的输出格式。

完整的操作演练，请参见 [LLM 步骤指南](/zh-cn/guides/workflows/llm-step/)。

## 配置

* **LLM 连接** *（必填）*——类型为 LLM 的连接（例如 Anthropic）。对于任何写入绑定，其**代理访问**必须为**读取和写入**。在 2027 年 1 月 15 日移除之前，**完整**同样允许写入，使用它的步骤在完成时会记录一条警告。在**读取和写入**级别下，步骤只会写入勾选了写入的绑定，且不能运行写入类 SQL 或创建表。
* **模型** *（可选）*——默认为连接的默认模型。使用 Anthropic 连接时，任何 Claude 模型都可使用，包括 Claude Sonnet 4.5 等较早的模型。
* **提示词** *（必填）*——支持用 `{{tables.NAME}}`、`{{dimensions.NAME}}` 和 `{{documents.NAME}}` 引用已绑定的对象。
* **Result schema** *（Anthropic 可选；其他提供方必填）*——用于捕获结构化摘要的 JSON 架构（根为 `"type": "object"`）；使用 Anthropic 时，如果模型的工作成果是其 MCP 写入，则留空。非 Anthropic 提供方没有 MCP 访问权限，因此必须提供架构。
* **Bindings**——模型可访问的表、维度和文档，每项都通过选择器选取，并授予**读取**和/或**写入**权限。写入表接收插入的行，写入维度接收节点，写入文档接收上传的文件。
* **限制**——Max output tokens 对应**最大输出令牌数**（1,024 到 128,000）和 Credential TTL（60 到 3,600 秒）。

## 行为

* 模型调用在独立的作业中运行。运行时会生成一个短期、限定范围的凭据，并在运行结束时撤销。
* 访问权限按对象和按复选框控制：模型只读取绑定了读取的对象，只写入绑定了写入的对象——绝不会触及您没有绑定的对象。写入要求目标对象已存在；步骤不会创建目标对象。
* 每次运行都会产生一次计费的提供方调用，并写入您绑定的对象。

## 保存时会检查什么

* **Result schema**——提供时，它必须是有效的 JSON、是 JSON 对象，并且在根上声明 `"type": "object"`。否则会拒绝保存，例如提示 *The result schema must declare "type": "object" at its root.*
* **Bindings 和连接**——只有 Anthropic 连接才会让模型访问绑定。将带有绑定的步骤保存到其他提供方的连接上会被拒绝，消息中会指明提供方，并要求您 *Remove the bindings or choose an Anthropic connection.* 勾选了**写入**的绑定需要一个**代理访问**允许写入的连接。在只读连接上，保存会被拒绝，并提示 *The selected LLM connection has Read-only Agent Access, so a binding with Write checked could not write. Set the connection to 'Read & write' or uncheck Write on the bindings.* 通过 API 保存的、没有连接的步骤，会按工作区的默认 LLM 连接进行检查，它也在该连接上运行：即管理员标记为默认的连接，否则是最近更新的连接。如果没有管理员标记的默认连接，编辑另一个 LLM 连接会使其成为默认连接，并可能导致该步骤下次保存被拒绝。
