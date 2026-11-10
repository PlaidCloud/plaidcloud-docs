---
title: 添加 AWS S3 账户
description: 将 AWS S3 存储账户添加到 PlaidCloud，以便使用 Amazon 云对象存储导入和导出数据文件。
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-aws-s3-account.md
---

## AWS S3 设置

这些步骤需要在 AWS 控制台中完成。

1. 登录或创建 Amazon Web Services (AWS) 账户
2. 在控制台中转到 `All services > Storage > S3`
3. 创建一个默认或测试存储桶。记下存储桶名称和区域（例如 `us-east-1`）。
4. 在控制台中转到 `All Services > Security Identity & Compliance > IAM > Users`
5. 选择 `Create User` 按钮
6. 出现提示时，输入用户名并仅选择 `Access Key - Programmatic access`。选择 `Next: Permissions` 按钮。
7. 选择名为 `Attach existing policies directly` 的选项框
8. 在筛选搜索框中输入 `s3`。当列表筛选为与 S3 相关的项目后，勾选左侧的复选框以选择 `AmazonS3FullAccess`。选择 `Next: Tags` 按钮。
9. 选择 `Next: Review` 按钮跳过此步骤
10. 检查用户设置并选择 `Create user`
11. 下载 CSV 或将密钥复制粘贴到某处，以保存为该用户生成的密钥供以后使用。此密钥无法再次获取，因此请妥善保管。如需重新生成密钥，只需返回上面的第 5 步。

现在，您已具备将 S3 账户添加到 PlaidCloud 文档所需的一切。


## PlaidCloud 文档设置

1. 登录 PlaidCloud
2. 选择新文档账户所在的工作区
3. 转到 `Document > Manage`
4. 选择**新建账户**按钮
5. 选择 `Amazon S3` 作为服务类型
6. 填写名称和描述
7. 在**起始路径**字段中输入存储桶名称和可选的路径前缀（例如 `my-bucket` 或 `my-bucket/data`）。路径的第一段是存储桶名称。
8. 为您的用例选择合适的**安全模型**。如果不确定，请保留为 `Private`。
9. 将上面第 11 步中创建的**访问密钥**粘贴到“身份验证凭据”下的“访问密钥 ID”字段中
10. 将上面第 11 步中创建的**机密密钥**粘贴到“身份验证凭据”下的“机密访问密钥”字段中
11. 输入存储桶的**区域**（例如 `us-east-1`、`eu-west-1`）。如果留空，则默认为 `us-east-2`。
12. 选择“保存”按钮，新的文档账户即可投入使用
