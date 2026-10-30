---
title: 添加 AWS S3 账户
description: 将 AWS S3 存储账户添加到 PlaidCloud，以使用亚马逊云对象存储导入和导出数据文件。
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-aws-s3-account.md
---

## AWS S3 设置

以下步骤需要在 AWS 控制台中完成。

1. 登录或创建 Amazon Web Services (AWS) 账户
2. 在控制台中转到 `All services > Storage > S3`
3. 创建默认存储桶或测试存储桶。记下存储桶名称和区域（例如 `us-east-1`）。
4. 在控制台中转到 `All Services > Security Identity & Compliance > IAM > Users`
5. 选择 `Create User` 按钮
6. 出现提示时，输入用户名，并仅选择 `Access Key - Programmatic access`。选择 `Next: Permissions` 按钮。
7. 选择名为 `Attach existing policies directly` 的选项框
8. 在筛选搜索框中输入 `s3`。当列表筛选为与 S3 相关的项时，勾选左侧的复选框以选择 `AmazonS3FullAccess`。选择 `Next: Tags` 按钮。
9. 选择 `Next: Review` 按钮以跳过此步骤
10. 查看用户设置并选择 `Create user`
11. 通过下载 CSV 或将密钥复制粘贴到某处以备后用，保存为该用户生成的密钥。您将无法再次检索此密钥，因此请妥善保管。如果需要重新生成密钥，只需返回上面的第 5 步。

现在，您应该已具备将 S3 账户添加到 PlaidCloud 文档所需的一切。


## PlaidCloud 文档设置

1. 登录 PlaidCloud
2. 选择新文档账户所在的工作区
3. 转到 `Document > Manage Accounts`
4. 选择 `+ New Account` 按钮
5. 选择 `Amazon S3` 作为服务类型
6. 填写名称和说明
7. 在 **起始路径** 字段中输入存储桶名称和可选的路径前缀（例如 `my-bucket` 或 `my-bucket/data`）。第一个路径段是存储桶名称。
8. 根据您的使用场景选择合适的 **安全模型**。如果不确定，请保持为 `Private`。
9. 将上面第 11 步中创建的 **Access Key** 粘贴到“身份验证凭据”下的“访问密钥 ID”字段中
10. 将上面第 11 步中创建的 **Secret Key** 粘贴到“身份验证凭据”下的“机密访问密钥”字段中
11. 输入存储桶的 **区域**（例如 `us-east-1`、`eu-west-1`）。如果留空，则默认为 `us-east-2`。
12. 选择“保存”按钮，您的新文档账户即可使用
