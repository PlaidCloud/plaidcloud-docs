---
title: 添加 Backblaze B2 账户
description: 将 Backblaze B2 存储账户添加到 PlaidCloud，以便使用经济实惠的云对象存储导入和导出数据文件。
sidebar:
  order: 8
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-backblaze-b2-account.md
---

## Backblaze B2 设置

这些步骤需要在 Backblaze B2 控制台中完成。

1. 登录 [Backblaze B2 控制台](https://secure.backblaze.com/b2_buckets.htm)
2. 导航到 **Buckets**，如果还没有存储桶，则创建一个。记下存储桶名称。
3. 导航到 **App Keys**
4. 选择 **Add a New Application Key**
5. 为密钥命名，选择它应有权访问的存储桶，并选择适当的权限（读取和写入）
6. 选择 **Create New Key**
7. 复制 **keyID**（即访问密钥）和 **applicationKey**（即机密密钥）。保存这两项，供下面的 PlaidCloud 文档设置使用。应用程序密钥只显示一次。
8. 记下存储桶所在区域的 **S3 Endpoint**。它遵循 `https://s3.{region}.backblazeb2.com` 格式（例如 `https://s3.us-west-004.backblazeb2.com`）。可以在存储桶详细信息页面上找到它。

现在，您已具备将 Backblaze B2 账户添加到 PlaidCloud 文档所需的一切。


## PlaidCloud 文档设置

1. 登录 PlaidCloud
2. 选择新文档账户所在的工作区
3. 转到 `Document > Manage`
4. 选择**新建账户**按钮
5. 选择 `Backblaze B2` 作为服务类型
6. 填写名称和描述
7. 将**起始路径**输入为 S3 兼容端点后跟存储桶名称：`https://s3.us-west-004.backblazeb2.com/my-bucket`
8. 输入存储桶的**区域**（例如 `us-west-004`）
9. 为您的用例选择合适的**安全模型**。如果不确定，请保留为 `Private`。
10. 将 **keyID** 粘贴到“身份验证凭据”下的“访问密钥 ID”字段中
11. 将 **applicationKey** 粘贴到“身份验证凭据”下的“机密访问密钥”字段中
12. 选择“保存”按钮，新的文档账户即可投入使用
