---
title: 添加 Cloudflare R2 账户
description: 将 Cloudflare R2 存储账户添加到 PlaidCloud，以使用 Cloudflare 零出口费用的对象存储导入和导出数据文件。
sidebar:
  order: 9
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-cloudflare-r2-account.md
---

## Cloudflare R2 设置

以下步骤需要在 Cloudflare 仪表板中完成。

1. 登录 [Cloudflare 仪表板](https://dash.cloudflare.com)
2. 选择您的账户，然后在左侧边栏中导航到 **R2 Object Storage**
3. 如果尚不存在存储桶，请创建一个。记下存储桶名称。
4. 导航到 **R2 Object Storage > Manage R2 API Tokens**
5. 选择 **Create API Token**
6. 为令牌命名，选择它应有权访问的存储桶，并选择 **Object Read & Write** 权限
7. 选择 **Create API Token**
8. 复制 **Access Key ID** 和 **Secret Access Key**。保存这两项，供下面的 PlaidCloud 文档设置使用。机密只显示一次。
9. 记下您账户的 **S3 API endpoint**。其格式为 `https://{account_id}.r2.cloudflarestorage.com`，显示在 R2 概览页面上。

现在，您应该已具备将 Cloudflare R2 账户添加到 PlaidCloud 文档所需的一切。


## PlaidCloud 文档设置

1. 登录 PlaidCloud
2. 选择新文档账户所在的工作区
3. 转到 `Document > Manage Accounts`
4. 选择 `+ New Account` 按钮
5. 选择 `Cloudflare R2` 作为服务类型
6. 填写名称和说明
7. 将 **起始路径** 输入为您的 R2 端点后跟存储桶名称：`https://{account_id}.r2.cloudflarestorage.com/my-bucket`
8. **区域** 字段可以设置为 `auto` 或留空，R2 会自动选择最近的区域
9. 根据您的使用场景选择合适的 **安全模型**。如果不确定，请保持为 `Private`。
10. 将 **Access Key ID** 粘贴到“身份验证凭据”下的“访问密钥 ID”字段中
11. 将 **Secret Access Key** 粘贴到“身份验证凭据”下的“机密访问密钥”字段中
12. 选择“保存”按钮，您的新文档账户即可使用
