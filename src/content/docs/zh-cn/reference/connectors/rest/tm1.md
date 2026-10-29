---
title: TM1 连接器
description: 通过 REST API 将 PlaidCloud 连接到 IBM TM1 / Planning Analytics 服务器，支持原生 Basic 身份验证或 CAM 命名空间身份验证；可云端直连，也可通过本地部署的 PlaidLink 代理访问云端无法直接到达的服务器。
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/tm1.md
---

通过已发布的 OData v4 REST API 将 PlaidCloud 连接到 IBM **TM1 / Planning Analytics** 服务器，无需 JVM 桥接，也无需 PAOlap 驱动程序。可使用 [TM1：查询多维数据集](/zh-cn/reference/workflow-steps/ibm-planning-analytics/tm1-query/)读取多维数据集数据，或使用 [TM1：读取维度](/zh-cn/reference/workflow-steps/ibm-planning-analytics/tm1-dimension-read/)读取 TM1 维度层次结构，两者均为云端直连；对于只能从您自己网络内部访问的 TM1 服务器，[TM1：查询多维数据集（代理）](/zh-cn/reference/workflow-steps/ibm-planning-analytics/tm1-query-remote/)会通过已安装的 PlaidLink 代理分派同样的读取操作。

该连接类型在连接选择器中显示为 **IBM Planning Analytics (TM1)**。

## 身份验证的工作方式

提供两种身份验证模式，与 TM1 自身的 REST 登录方案一致：

- **Native**：使用 TM1 用户名和密码的 HTTP Basic 身份验证。
- **CAM**：限定于某个命名空间的 IBM Cognos Access Manager 单点登录。请求携带由用户名、密码和命名空间共同构成的 `Authorization: CAMNamespace` 标头，与普通 Basic 不同。

目前尚不支持 PlanningAnalytics-as-a-Service (PAaaS) 的持有者令牌登录，仅支持上述两种 REST 登录方案。

## 配置

| 字段 | 必填 | 说明 |
|---|---|---|
| 名称 | 是 | 此连接的显示名称。 |
| 主机 | 是 | TM1 REST API 主机，例如 `https://tm1-prod.example.com:8010` 或 PAaaS URL。 |
| 默认数据库 | 否 | 为 TM1：查询多维数据集步骤的“数据库”字段预填的便捷值。各步骤可单独覆盖。 |
| 身份验证模式 | 是 | `Native`（TM1 用户/密码）或 `CAM`（Cognos Access Manager 单点登录）。默认为 Native。 |
| 用户名 | 是 | 用于身份验证的 TM1 账户。 |
| 密码 | 是 | 加密存储。 |
| CAM 命名空间 | 仅 CAM 模式需要 | 用于身份验证的 Cognos Access Manager 命名空间。在 Native 模式下不使用。 |
| 验证 SSL 证书 | 否 | 默认开启。仅在测试服务器使用已知的自签名证书时才关闭。 |
| 超时（秒） | 否 | 默认为 30。 |

## 测试连接

**测试连接**会探测服务器的 `Configuration` 单例（`GET {host}/api/v1/Configuration`），这是 TM1 提供的开销最小的已验证调用，且不需要数据库或多维数据集上下文。测试成功时会报告服务器的 **`ProductVersion`**，既确认主机可达，也确认凭据可通过身份验证。

## 只读

此连接器为只读。它从 TM1 读取多维数据集数据和维度层次结构，不会向 TM1 写入、过账或回写运行 TI 进程。

## 使用该连接可以做什么

- **按已保存视图或 MDX 读取多维数据集数据。** [TM1：查询多维数据集](/zh-cn/reference/workflow-steps/ibm-planning-analytics/tm1-query/)步骤运行命名的多维数据集视图或原始 MDX 查询，应用可选的观察点切片，并将结果落地为表。
- **将 TM1 层次结构加载为 PlaidCloud 维度。** [TM1：读取维度](/zh-cn/reference/workflow-steps/ibm-planning-analytics/tm1-dimension-read/)步骤读取维度的元素、父子边和属性，并据此构建 PlaidCloud 维度。
- **按期间切片进行增量提取。** TM1 没有内置的变更跟踪，因此只需要新数据的工作流可按期间或版本缩小查询范围，具体模式请参见步骤参考。
- **以云端直连方式实时发现多维数据集、视图和维度。** 步骤表单中的“多维数据集”“视图”和“维度”选取器会直接查询已连接的服务器，因此可以选择真实名称，而无需盲目输入。
- **通过本地部署的代理读取云端无法到达的 TM1 服务器。** 请参见下文的[读取防火墙后的 TM1](#读取防火墙后的-tm1)。

## 读取防火墙后的 TM1

如果 TM1 服务器只能从您自己的网络内部访问（没有公共端点、没有加入白名单的 IP，也没有通向 PlaidCloud 的 VPN），则需要通过已安装的 **PlaidLink 代理**访问，而不是云端直连。[TM1：查询多维数据集（代理）](/zh-cn/reference/workflow-steps/ibm-planning-analytics/tm1-query-remote/)工作流步骤会运行与 TM1：查询多维数据集相同的视图/MDX/观察点查询，但会将其分派给代理，由代理在您的网络中访问 TM1 并返回结果。

此方式需要：

- **已安装的 PlaidLink 代理**，且所在机器能够访问 TM1 服务器。请参见[安装 PlaidLink](/zh-cn/reference/cli/plaidlink/install/)。
- **包含 TM1 处理程序的代理版本。** PlaidCloud 在向代理分派查询之前会检查其公布的功能，因此较旧的代理版本在重新构建并重新安装之前无法处理 TM1 请求，PlaidLink 不会自动更新。请参见[升级 PlaidLink](/zh-cn/reference/cli/plaidlink/upgrade/)。
- **将此 TM1 连接共享给该代理**，这是在其已有的成员/分组访问权限之外，通过连接的 `Actions > Agents` 列表完成的。请参见[安全模型](/zh-cn/guides/connections/create-connection/#安全模型)。

TM1：查询多维数据集（代理）不支持实时发现，因为代理只在运行期间可达，而在步骤表单打开时不可达，所以多维数据集、视图和 MDX 需要手动输入，并在步骤运行时进行验证。TM1：读取维度仅支持云端直连，目前没有本地部署路径。

## 已知限制

| 限制 | 含义 |
|---|---|
| 只读 | 不支持回写，也不支持执行 TI 进程。 |
| 本地部署仅支持查询 | 本地部署的 PlaidLink 代理路径只涵盖多维数据集读取（TM1：查询多维数据集（代理））。TM1：读取维度目前没有本地部署路径，需要 PlaidCloud 能直接访问的网络路径。 |
| 维度读取仅支持单一层次结构、单一父级 | 元素位于多个父级之下的 TM1 层次结构无法加载为 PlaidCloud 维度，并且合并权重的大小（0.5、2.0）无法表示，只保留其符号。请参见 [TM1：读取维度](/zh-cn/reference/workflow-steps/ibm-planning-analytics/tm1-dimension-read/#此步骤无法表示的内容)。 |
| 不支持 PAaaS 持有者令牌身份验证 | 仅支持 Native (Basic) 和 CAM 身份验证。 |

## 相关内容

- [连接到 TM1（指南）](/zh-cn/guides/connections/tm1/)：创建连接并构建查询。
- [TM1：查询多维数据集](/zh-cn/reference/workflow-steps/ibm-planning-analytics/tm1-query/)：多维数据集读取，云端直连。
- [TM1：查询多维数据集（代理）](/zh-cn/reference/workflow-steps/ibm-planning-analytics/tm1-query-remote/)：通过本地部署的代理读取多维数据集。
- [TM1：读取维度](/zh-cn/reference/workflow-steps/ibm-planning-analytics/tm1-dimension-read/)：将 TM1 层次结构加载为 PlaidCloud 维度。
- [创建和管理连接](/zh-cn/guides/connections/create-connection/)
