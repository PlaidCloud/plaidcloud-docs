---
title: 添加 Cloudflare R2 账户
description: 将 Cloudflare R2 存储账户添加到 PlaidCloud，以便使用 Cloudflare 免出口费用的对象存储导入和导出数据文件。
sidebar:
  order: 9
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-cloudflare-r2-account.md
---

## Cloudflare R2 设置

这些步骤需要在 Cloudflare 控制面板中完成。

1. 登录 [Cloudflare 控制面板](https://dash.cloudflare.com)
2. 选择您的账户，然后在左侧边栏中导航到 **R2 Object Storage**
3. 如果还没有存储桶，则创建一个。记下存储桶名称。
4. 导航到 **R2 Object Storage > Manage R2 API Tokens**
5. 选择 **Create API Token**
6. 为令牌命名，选择它应有权访问的存储桶，并选择 **Object Read & Write** 权限
7. 选择 **Create API Token**
8. 复制 **Access Key ID** 和 **Secret Access Key**。保存这两项，供下面的 PlaidCloud 文档设置使用。机密只显示一次。
9. 记下账户的 **S3 API endpoint**。它遵循 `https://{account_id}.r2.cloudflarestorage.com` 格式，显示在 R2 概览页面上。

现在，您已具备将 Cloudflare R2 账户添加到 PlaidCloud 文档所需的一切。


## PlaidCloud 文档设置

1. 登录 PlaidCloud
2. 选择新文档账户所在的工作区
3. 转到 `Document > Manage`
4. 选择**新建账户**按钮
5. 选择 `Cloudflare R2` 作为服务类型
6. 填写名称和描述
7. 将**起始路径**输入为 R2 端点后跟存储桶名称：`https://{account_id}.r2.cloudflarestorage.com/my-bucket`
8. **区域**字段可以设置为 `auto` 或留空，R2 会自动选择最近的区域
9. 为您的用例选择合适的**安全模型**。如果不确定，请保留为 `Private`。
10. 将**访问密钥 ID** 粘贴到“身份验证凭据”下的“访问密钥 ID”字段中
11. 将**机密访问密钥**粘贴到“身份验证凭据”下的“机密访问密钥”字段中
12. 选择“保存”按钮，新的文档账户即可投入使用
