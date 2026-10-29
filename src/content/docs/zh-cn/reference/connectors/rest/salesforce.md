---
title: Salesforce REST 连接器
description: 在 PlaidCloud 中使用 OAuth 2.0 客户端凭据流程设置 Salesforce REST API 连接，对其进行测试，并通过 Salesforce 查询对象步骤将 CRM 对象拉取到项目表中。
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/salesforce.md
---

## API 文档

[Salesforce REST API 参考](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_what_is_rest_api.html)记录了记录和元数据端点，[Bulk API 2.0 开发者指南](https://developer.salesforce.com/docs/atlas.en-us.api_asynch.meta/api_asynch/bulk_api_2_0.htm)记录了 [Salesforce：查询对象](/zh-cn/reference/workflow-steps/salesforce/query-salesforce-object/)步骤所运行的查询作业。

如需从头到尾的操作说明（Salesforce 端的应用、Run As 用户、创建连接以及测试连接），请参阅[连接到 Salesforce](/zh-cn/guides/connections/salesforce/)指南。本页是其背后的字段参考。

## 身份验证的工作方式

该连接器使用 **OAuth 2.0 客户端凭据**登录：PlaidCloud 向组织自己的令牌端点，用应用的使用者密钥和密文换取访问令牌，并以应用在其 **Run As** 设置中指定的用户身份调用 API。不涉及交互式登录，没有刷新令牌，也无需管理证书。

该交换过程有两个实际中很重要的特性：

- **一个令牌覆盖整个提取。** PlaidCloud 按连接和环境缓存访问令牌，直到其即将过期，因此大型分页读取不会在每一页都重新进行身份验证。如果 Salesforce 提前停止承认某个令牌（被撤销、IP 限制或会话策略变更），该令牌会被丢弃并自动替换一次。
- **请求发往 Salesforce 指定的地址。** 令牌响应会指明组织的实例，之后的每次调用都针对该实例，而不是您输入的主机，因此 My Domain 或实例变更后连接仍可继续工作。

REST API 版本按连接固定，而不是浮动，因此组织升级不会悄悄改变已保存步骤下方的响应结构。新连接使用当前受支持的版本；可以通过连接配置 API 将连接固定到其他版本，如果固定的版本到达生命周期终点，Salesforce 会返回 HTTP 410，PlaidCloud 会报告被停用的是哪个版本。

## 配置

在 **Tools > Connections** 中创建或编辑 Salesforce 连接时会显示以下字段。

### 账户描述

| 字段 | 类型 | 说明 |
|---|---|---|
| 账户名称 | 文本 | 此连接的显示名称。 |
| 备注 | 文本（多行） | 关于该连接的可选备注。 |

### 连接

| 字段 | 类型 | 说明 |
|---|---|---|
| 主机或 IP 地址 | 文本 | 组织的 My Domain 主机：生产和 Developer Edition 为 `mycompany.my.salesforce.com`，沙盒为 `mycompany--uat.sandbox.my.salesforce.com`。如果您省略 `https://`，PlaidCloud 会自动添加。 |

### 身份验证凭据

| 字段 | 类型 | 说明 |
|---|---|---|
| 客户端 ID | 文本 | 应用的使用者密钥。 |
| 客户端密钥 | 密码 | 应用的使用者密文。加密保存；输入新值可更改，留空则保留已存储的值。 |

### 用法与安全

| 字段 | 类型 | 说明 |
|---|---|---|
| 启用（允许访问） | 开关 | 连接是否可用。清除该选项可暂停访问而不删除连接。 |
| 安全模型 | 选择 | 谁可以使用该连接：仅其所有者、指定成员、指定安全组，或所有工作区成员。 |

每个连接在每个环境中各保存一组这些值，因此一个连接可以在开发环境中指向沙盒，在生产环境中指向生产。请按环境分别测试并设置凭据。

## 测试连接

**测试连接**会执行真实的令牌交换，并报告凭据所对应的身份：

| 报告项 | 重要性 |
|---|---|
| 组织 ID | 确认凭据连接到哪个组织，是发现沙盒凭据被保存到生产环境的最快方式。 |
| API 版本 | 该组织支持的最高版本。读取在固定于连接的版本上运行（除非设置了 `salesforce_api_version`，否则为 `v61.0`），而不是此版本。 |
| Run As 用户 | 该连接返回的每一行和每个字段都以此用户的权限为范围。在信任提取的行数之前请先检查这一项。 |

失败的测试会指明原因。身份验证失败会报告 HTTP 状态，并提示您重新输入客户端 ID 和密钥，因为客户端密钥一旦保存就无法回读。

## 已知限制

- **Run As 用户以两种不同方式限定每次读取的范围。** 该用户看不到的行会直接缺失，没有错误，也没有计数。该用户无法读取的字段会导致整个查询失败。两者均在[Run As 用户限定一切范围](/zh-cn/guides/connections/salesforce/#run-as-用户决定一切范围)中说明。
- **仅限读取。** 此连接器提取数据，不会将记录写回 Salesforce。
- **某些字段类型无法提取**，包括复合地址和地理位置字段、`base64` 二进制大对象、`encryptedstring` 和 `anyType`。步骤的字段选择器会标记每一种并说明原因。请参阅[步骤拒绝的字段](/zh-cn/reference/workflow-steps/salesforce/query-salesforce-object/#步骤拒绝的字段)。
- **提取不等于同步。** 在 Salesforce 中删除的记录会保留在目标表中。

## 相关内容

- [连接到 Salesforce](/zh-cn/guides/connections/salesforce/) — 分步说明
- [Salesforce：查询对象](/zh-cn/reference/workflow-steps/salesforce/query-salesforce-object/)
- [创建和管理连接](/zh-cn/guides/connections/create-connection/)
