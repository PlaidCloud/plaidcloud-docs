---
title: 添加 PlaidCloud 托管存储桶账户
description: 一步为 PlaidCloud 文档添加完全托管的文件存储：只需选择名称，PlaidCloud 会为您完成所有设置，无需任何配置。
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-managed-bucket-account.md
---

**PlaidCloud 托管存储桶**是为文档添加文件存储的最快方式。PlaidCloud 为您创建并运行存储，无需事先设置，也无需管理凭据。您只需为它命名。

当您想要一个新的、独立的位置来保存文档文件时，请使用 PlaidCloud 托管存储桶。如需连接您自己拥有并自行管理的存储，请改为在[添加新文档账户](/zh-cn/guides/documents/adding-accounts/)页面上选择其他提供商之一。

## 设置

1. 登录 PlaidCloud
2. 选择新文档账户所在的工作区
3. 转到 `Document > Manage Accounts`
4. 选择 `+ New Account` 按钮
5. 选择 `PlaidCloud Managed Bucket` 作为服务类型
6. 填写名称和可选的说明
7. 输入 **存储桶名称**。名称长度必须为 3 到 63 个字符，只能使用小写字母、数字、点或连字符，并且必须以字母或数字开头和结尾。名称必须**全局唯一**，如果已被占用，系统会要求您另选一个
8. 根据您的使用场景选择合适的 **安全模型**。如果不确定，请保持为 `Private`
9. 选择“保存”按钮

PlaidCloud 会设置好存储，并让您成为其所有者。该账户可立即浏览和上传，无需其他配置。

:::note
PlaidCloud 托管存储桶适用于 **Business** 和 **Enterprise** 套餐。如果您的套餐不包含它们，或者已达到套餐的上限，在您尝试创建时，表单会给出提示。
:::

## 创建之后

- 存储桶名称一经创建即固定，现有账户上无法更改。
- 删除账户会**将存储的文件保留在原处**，因此删除绝不会销毁您的数据。如果需要移除存储本身，请联系支持人员。
- PlaidCloud 托管存储桶在[访问控制](/zh-cn/guides/documents/account-management/control-document-account-access/)、[所有权](/zh-cn/guides/documents/account-management/managing-document-account-owners/)和浏览方面，与其他任何文档账户的行为相同。
