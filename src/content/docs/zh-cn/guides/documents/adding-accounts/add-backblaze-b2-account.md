---
title: 添加 Backblaze B2 账户
description: 将 Backblaze B2 存储账户添加到 PlaidCloud，以使用经济实惠的云对象存储导入和导出数据文件。
sidebar:
  order: 8
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-backblaze-b2-account.md
---

## Backblaze B2 设置

以下步骤需要在 Backblaze B2 控制台中完成。

1. 登录 [Backblaze B2 控制台](https://secure.backblaze.com/b2_buckets.htm)
2. 导航到 **Buckets**，如果尚不存在存储桶，请创建一个。记下存储桶名称。
3. 导航到 **App Keys**
4. 选择 **Add a New Application Key**
5. 为密钥命名，选择它应有权访问的存储桶，并选择适当的权限（读取和写入）
6. 选择 **Create New Key**
7. 复制 **keyID**（即您的访问密钥）和 **applicationKey**（即您的机密密钥）。保存这两项，供下面的 PlaidCloud 文档设置使用。应用程序密钥只显示一次。
8. 记下存储桶所在区域的 **S3 Endpoint**。其格式为 `https://s3.{region}.backblazeb2.com`（例如 `https://s3.us-west-004.backblazeb2.com`）。可在存储桶详细信息页面上找到。

现在，您应该已具备将 Backblaze B2 账户添加到 PlaidCloud 文档所需的一切。


## PlaidCloud 文档设置

1. 登录 PlaidCloud
2. 选择新文档账户所在的工作区
3. 转到 `Document > Manage Accounts`
4. 选择 `+ New Account` 按钮
5. 选择 `Backblaze B2` 作为服务类型
6. 填写名称和说明
7. 将 **起始路径** 输入为您的 S3 兼容端点后跟存储桶名称：`https://s3.us-west-004.backblazeb2.com/my-bucket`
8. 输入存储桶的 **区域**（例如 `us-west-004`）
9. 根据您的使用场景选择合适的 **安全模型**。如果不确定，请保持为 `Private`。
10. 将 **keyID** 粘贴到“身份验证凭据”下的“访问密钥 ID”字段中
11. 将 **applicationKey** 粘贴到“身份验证凭据”下的“机密访问密钥”字段中
12. 选择“保存”按钮，您的新文档账户即可使用
