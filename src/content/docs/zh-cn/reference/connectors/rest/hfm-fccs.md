---
title: HFM / FCCS 连接器
description: 在 PlaidCloud 中设置 Oracle FCCS（Financial Consolidation and Close，EPM Cloud）连接，通过视角选择器自助获取临时数据切片，并可选启用缓存和定期计划加载。
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/hfm-fccs.md
---

将 PlaidCloud 连接到 Oracle **FCCS**（Financial Consolidation and Close，Oracle EPM Cloud 的一部分），使财务用户无需向 HFM 团队提交工单即可自助获取数据切片。[HFM/FCCS：读取数据（临时）](/zh-cn/reference/workflow-steps/oracle-epm/hfm-fccs-read/)步骤使用起来就像实时查询，但在底层，它是针对 FCCS 数据导出作业 API 的异步请求 → 轮询 → 获取流程。

该连接类型在连接选择器中显示为 **REST - HFM/FCCS**。

:::note[限定实体维度的范围]
请始终限定每个视角的范围。未限定范围的提取在导出作业运行期间可能长时间锁定 FCCS 应用程序。
:::

## API 文档

该连接器使用 Oracle EPM Cloud 的 [REST API](https://docs.oracle.com/en/cloud/saas/enterprise-performance-management-common/prest/index.html)，包括应用程序元数据端点（用于发现维度和成员）和数据导出作业端点（用于请求、轮询和获取网格）。

## 身份验证的工作方式

该连接在经典 EPM Cloud 实例上使用**带服务账号的 HTTP 基本身份验证**，不涉及 OAuth 或令牌流程（OCI / Gen 2 持有者令牌实例不在支持范围内）。设置了**身份域**时，PlaidCloud 会将登录名组合为 `identitydomain.username`（域、一个点，然后是用户名）；如果将身份域留空，或用户名本身已包含点，则按原样发送用户名。请将连接指向专用的集成服务账号，该账号需对自助用户将要拉取的应用程序和视角切片具有读取权限。

## 配置

| 字段 | 必填 | 说明 |
|---|---|---|
| 名称 | 是 | 此连接的显示名称。 |
| EPM Cloud URL | 是 | 您的 EPM Cloud 实例/服务 URL，例如 `https://planning-test-yourdomain.epm.us2.oraclecloud.com`。 |
| 身份域 | 否 | 您的 EPM Cloud 身份域。设置后，PlaidCloud 在登录时会将其作为前缀添加到用户名前，形如 `identitydomain.username`。 |
| 用户名 | 是 | 集成服务账号的用户名。 |
| 密码 | 是 | 服务账号的密码。加密存储。 |
| 默认应用程序 | 否 | 在步骤的视角选择器中预填的默认 FCCS 应用程序。每个步骤都可以覆盖它。 |

## 使用该连接可以做什么

- **自助获取临时切片。** 在步骤表单中构建视角（POV），即应用程序加上 FCCS 维度，点击“运行”，结果表便会自动生成。请参阅 [HFM/FCCS：读取数据（临时）](/zh-cn/reference/workflow-steps/oracle-epm/hfm-fccs-read/)。
- **无需提交工单。** 切片以连接的服务账号运行，因此财务用户可以自行拉取数据，而不必等待 HFM 管理员。
- **缓存重复拉取。** 再次请求相同的视角和截至日期时，会立即返回已加载的副本，而不是再次访问 FCCS。
- **管控谁能看到哪些实体。** 已加载的表**支持行级安全**：管理员可以在 `Entity` 列上声明行访问权限，使自助用户只能看到其有权访问的实体。这由管理员控制，并非自动生效，请参阅步骤参考。
- **计划定期加载。** 启用**限定目标**，可将临时切片提升为持久表，该表以追加方式增长并通过合并而非覆盖来更新，因此将同一步骤放入计划工作流即可成为每晚运行的定期加载。

## 元数据发现

在受支持的 FCCS 实例上，选择连接和应用程序后，步骤表单会从应用程序元数据中实时发现每个维度的成员列表，因此视角选择器会提供真实成员供选择（任一选择更改时都会重新发现）。在不提供元数据端点的较旧实例上，发现不会返回任何内容，选择器会回退为手动输入，即手动输入成员名称，已保存的视角始终可以完整往返。两种方式下拉取的工作方式相同。

## 已知限制

| 限制 | 含义 |
|---|---|
| 只读 | 该连接器从 FCCS 提取数据。它不会写入合并数据、运行合并或回写过账。 |
| 限定实体维度的范围 | 未限定范围的提取（未选择 `Entity`）在导出作业运行期间可能长时间锁定 FCCS 应用程序。请始终限定实体选择范围。 |
| 较旧实例上需手动输入成员 | 如果实例不提供元数据端点，成员列表不会自动填充，请手动输入成员名称。 |
| 行级安全由管理员管控，而非自动生效 | 已加载的表可以通过行访问权限进行管控，但管理员必须发布、声明 `Entity` 列、批准首次受管控的写入并进行协调。在此之前，表不会被筛选。 |

## 相关内容

- [从 HFM / FCCS 提取（指南）](/zh-cn/guides/connections/hfm-fccs/) — 创建连接、构建视角、运行、缓存、管控和计划。
- [HFM/FCCS：读取数据（临时）](/zh-cn/reference/workflow-steps/oracle-epm/hfm-fccs-read/) — 步骤字段参考。
- [管理安全组和分配](/zh-cn/administration/access/managing-security-groups-and-assignments/) — 行访问权限如何管控已加载的表。
- [创建和管理连接](/zh-cn/guides/connections/create-connection/)
