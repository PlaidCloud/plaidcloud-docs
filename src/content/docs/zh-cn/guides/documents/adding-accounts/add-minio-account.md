---
title: 添加 MinIO 账户
description: 将 MinIO 存储账户添加到 PlaidCloud，使用自托管的 S3 兼容对象存储导入和导出数据文件。
sidebar:
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-minio-account.md
---

## MinIO 设置

以下步骤需要在 MinIO Console 中或通过 `mc` CLI 完成。

1. 登录 MinIO Console（例如 `https://your-minio-host:9001`）
2. 导航到 **Buckets**，如果尚无存储桶则创建一个，并记下存储桶名称。
3. 导航到 **Identity > Users**（或 **Access Keys**）
4. 创建对目标存储桶具有读写权限的新用户或服务账户
5. 复制为该用户生成的 **Access Key** 和 **Secret Key**，并保存好这两项，供下面的 PlaidCloud 文档设置使用。
6. 记下 MinIO 端点 URL（例如 `https://play.min.io` 或 `https://minio.yourcompany.com`）

现在，您已具备将 MinIO 账户添加到 PlaidCloud 文档所需的全部信息。


## PlaidCloud 文档设置

1. 登录 PlaidCloud
2. 选择新文档账户所在的工作区
3. 转到 `Document > Manage Accounts`
4. 选择 `+ New Account` 按钮
5. 选择 `MinIO` 作为服务类型
6. 填写名称和说明
7. 在**起始路径**中输入 MinIO 端点 URL，后接存储桶名称和可选前缀：`https://minio.yourcompany.com/my-bucket/optional/prefix`
8. 如果 MinIO 部署使用区域，请输入**区域**；否则留空
9. 根据使用场景选择合适的**安全模型**。不确定时保留 `Private`。
10. 在身份验证凭据下，将 **Access Key** 粘贴到访问密钥 ID 字段
11. 在身份验证凭据下，将 **Secret Key** 粘贴到机密访问密钥字段
12. 选择“保存”按钮，新的文档账户即可使用
