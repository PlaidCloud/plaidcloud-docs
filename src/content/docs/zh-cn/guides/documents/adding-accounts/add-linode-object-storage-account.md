---
title: 添加 Linode Object Storage 账户
description: 将 Linode (Akamai) Object Storage 账户添加到 PlaidCloud，以使用 Linode 的 S3 兼容云存储导入和导出数据文件。
sidebar:
  order: 11
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-linode-object-storage-account.md
---

## Linode Object Storage 设置

以下步骤需要在 Linode Cloud Manager 中完成。

1. 登录 [Linode Cloud Manager](https://cloud.linode.com)
2. 在左侧边栏中导航到 **Object Storage**
3. 如果尚不存在存储桶，请创建一个。记下存储桶名称（称为 **label**）和区域（例如 `us-east-1`）。
4. 导航到 **Object Storage > Access Keys**
5. 选择 **Create Access Key**
6. 为密钥指定一个标签，并选择它应有权访问的、具有读写权限的存储桶
7. 选择 **Create Access Key**
8. 复制 **Access Key** 和 **Secret Key**。保存这两项，供下面的 PlaidCloud 文档设置使用。机密只显示一次。
9. 记下存储桶所在区域的端点 URL。其格式为 `https://{region}.linodeobjects.com`（例如 `https://us-east-1.linodeobjects.com`）

现在，您应该已具备将 Linode Object Storage 账户添加到 PlaidCloud 文档所需的一切。


## PlaidCloud 文档设置

1. 登录 PlaidCloud
2. 选择新文档账户所在的工作区
3. 转到 `Document > Manage Accounts`
4. 选择 `+ New Account` 按钮
5. 选择 `Linode Object Storage` 作为服务类型
6. 填写名称和说明
7. 将 **起始路径** 输入为端点 URL 后跟存储桶名称：`https://us-east-1.linodeobjects.com/my-bucket`
8. 输入 **区域**（例如 `us-east-1`）
9. 根据您的使用场景选择合适的 **安全模型**。如果不确定，请保持为 `Private`。
10. 将 **Access Key** 粘贴到“身份验证凭据”下的“访问密钥 ID”字段中
11. 将 **Secret Key** 粘贴到“身份验证凭据”下的“机密访问密钥”字段中
12. 选择“保存”按钮，您的新文档账户即可使用
