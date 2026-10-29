---
title: 添加 DigitalOcean Spaces 账户
description: 将 DigitalOcean Spaces 存储账户添加到 PlaidCloud，以使用 DigitalOcean 的 S3 兼容对象存储导入和导出数据文件。
sidebar:
  order: 10
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-digitalocean-spaces-account.md
---

## DigitalOcean Spaces 设置

以下步骤需要在 DigitalOcean 控制面板中完成。

1. 登录 [DigitalOcean 控制面板](https://cloud.digitalocean.com)
2. 在左侧边栏中导航到 **Spaces Object Storage**
3. 如果尚不存在 Space，请创建一个。记下 Space 名称和区域（例如 `nyc3`）。
4. 导航到 **API > Spaces Keys**（位于 Tokens 部分下）
5. 选择 **Generate New Key**
6. 为密钥命名
7. 复制 **Key**（访问密钥）和 **Secret**。保存这两项，供下面的 PlaidCloud 文档设置使用。机密只显示一次。
8. 记下 Space 所在区域的端点 URL。其格式为 `https://{region}.digitaloceanspaces.com`（例如 `https://nyc3.digitaloceanspaces.com`）

现在，您应该已具备将 DigitalOcean Spaces 账户添加到 PlaidCloud 文档所需的一切。


## PlaidCloud 文档设置

1. 登录 PlaidCloud
2. 选择新文档账户所在的工作区
3. 转到 `Document > Manage Accounts`
4. 选择 `+ New Account` 按钮
5. 选择 `DigitalOcean Spaces` 作为服务类型
6. 填写名称和说明
7. 将 **起始路径** 输入为端点 URL 后跟 Space 名称：`https://nyc3.digitaloceanspaces.com/my-space`
8. 输入 **区域**（例如 `nyc3`、`sfo3`、`ams3`）
9. 根据您的使用场景选择合适的 **安全模型**。如果不确定，请保持为 `Private`。
10. 将 **Key** 粘贴到“身份验证凭据”下的“访问密钥 ID”字段中
11. 将 **Secret** 粘贴到“身份验证凭据”下的“机密访问密钥”字段中
12. 选择“保存”按钮，您的新文档账户即可使用
