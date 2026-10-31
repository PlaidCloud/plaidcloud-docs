---
title: "TM1：查询多维数据集（代理）"
description: "从云端无法直接访问的本地 IBM TM1 / Planning Analytics 服务器读取多维数据集切片——与 TM1：查询多维数据集相同的视图/MDX/视点查询，通过已安装的 PlaidLink 代理调度。"
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/ibm-planning-analytics/tm1-query-remote.md
---

## 说明

[TM1：查询多维数据集](/zh-cn/reference/workflow-steps/ibm-planning-analytics/tm1-query/)的本地对应版本：相同的读取——针对 TM1 多维数据集的已保存**视图**或 **MDX** 查询，可选视点 (POV) 切片，结果加载为项目表——但通过您网络中已安装的 [PlaidLink 代理](/zh-cn/reference/cli/plaidlink/)调度，而不是云端直连调用。当 TM1 服务器只能从您自己的网络内部访问时，请使用此步骤，而不是 TM1：查询多维数据集。

此步骤在步骤菜单中位于 **IBM TM1 / Planning Analytics** 下。

## 与 TM1：查询多维数据集的区别

| | TM1：查询多维数据集 | TM1：查询多维数据集（代理） |
|---|---|---|
| 传输方式 | 通过 REST 云端直连 | 调度到您网络中的 PlaidLink 代理 |
| 配置字段 | — | 相同，另加必填的**代理** |
| 多维数据集/视图发现 | 实时，来自已连接的数据库 | 不可用——请手动输入名称 |
| 保存前预览 | 是 | 不可用 |

其他一切——连接、数据库、视图/MDX 选择、视点切片、隐藏零值/空单元格、行数限制，以及按期间的增量提取模式——都与 [TM1：查询多维数据集](/zh-cn/reference/workflow-steps/ibm-planning-analytics/tm1-query/)页面所述完全一致。只有下面的差异是此步骤特有的。

## 配置

### 源和目标

| 字段 | 是否必填 | 说明 |
|---|---|---|
| 代理 | 是 | 将此读取调度到的 PlaidLink 代理。其构建版本必须包含 TM1 处理程序（参见下文的[要求](#要求)）。 |
| TM1 连接 | 是 | 用于读取的 [TM1 连接](/zh-cn/guides/connections/tm1/)。连接选择器不会按所选代理过滤——请另行将连接共享给代理（见下文）。 |
| 环境 | 是 | 连接的环境。 |
| 数据库 | 是 | 要查询的 TM1 数据库（实例）。 |
| 多维数据集 | 是 | 要查询的 TM1 多维数据集。手动输入——此步骤没有实时发现。 |
| 目标表 | 是 | 返回的单元格集所写入的项目表。 |

### 切片和选项

字段与 [TM1：查询多维数据集](/zh-cn/reference/workflow-steps/ibm-planning-analytics/tm1-query/#切片)相同——源模式（按视图/按 MDX）、视图、MDX、视点、隐藏零值/空单元格和行数限制——均为手动输入而非实时发现，并且都在步骤运行时而不是在预览中验证。

## 不支持经代理的发现

TM1：查询多维数据集的多维数据集、视图和维度选择器会在您编辑步骤时实时查询已连接的服务器。此步骤不存在这种实时发现：代理只在运行期间可访问，而不是在浏览器中打开表单时。多维数据集、视图和 MDX 均为手动输入，无法识别的名称会使运行带着清晰的错误失败，而不是悄悄失败。出于同样的原因，没有**预览**按钮——预览需要访问 TM1，而只有代理才能做到。

## 要求

读取本地 TM1 服务器需要：

- **已安装的 PlaidLink 代理**，所在机器可通过网络访问 TM1 服务器。参见[安装 PlaidLink](/zh-cn/reference/cli/plaidlink/install/)。
- **包含 TM1 处理程序的该代理构建版本。** PlaidCloud 会在调度前检查代理公布的功能；构建早于此功能的代理无法处理该请求。**PlaidLink 不会自动更新**——现有代理必须手动重新构建/重新安装才能获得 TM1 支持。参见[升级 PlaidLink](/zh-cn/reference/cli/plaidlink/upgrade/)。
- **与该代理共享的 TM1 连接**，这是在其已有的成员/分组访问权限之外另行授予的——请在连接的 `Actions > Agents` 列表中授予。参见[安全模型](/zh-cn/guides/connections/create-connection/#安全模型)。

## 相关内容

- [TM1：查询多维数据集](/zh-cn/reference/workflow-steps/ibm-planning-analytics/tm1-query/)——此步骤所对应的云端直连版本。
- [TM1：读取维度](/zh-cn/reference/workflow-steps/ibm-planning-analytics/tm1-dimension-read/)——云端直连，将 TM1 层次结构加载到 PlaidCloud 维度中。
- [连接到 TM1（指南）](/zh-cn/guides/connections/tm1/)——创建连接。
- [TM1 连接器](/zh-cn/reference/connectors/rest/tm1/)——连接字段参考，包括本地代理路径。
- [PlaidLink](/zh-cn/reference/cli/plaidlink/)——安装和升级代理。
- [IBM TM1 / Planning Analytics 步骤](/zh-cn/reference/workflow-steps/ibm-planning-analytics/)
