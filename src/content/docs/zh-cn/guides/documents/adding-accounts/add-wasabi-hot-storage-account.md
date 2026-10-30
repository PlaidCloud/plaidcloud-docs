---
title: 添加 Wasabi Hot Storage 账户
description: 将 Wasabi Hot Storage 账户添加到 PlaidCloud，使用高性价比的云存储导入和导出数据文件。
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-wasabi-hot-storage-account.md
---

## Wasabi Hot Storage 设置


以下步骤需要在 Wasabi Hot Storage 控制台中完成


1. 登录或创建 Wasabi Hot Storage 账户
2. 在控制台中转到 `Buckets`
3. 创建默认存储桶或测试存储桶
4. 在控制台中转到 Users
5. 选择 `Create User` 按钮
6. 出现提示时，输入用户名并选择 `Programmatic (create API key)` 用户
7. 跳过分组分配，选择 `Next` 按钮
8. 选择 `WasabiFullAccess` 策略旁边的加号图标，将该策略附加到用户，然后选择 `Next` 按钮。
9. 检查用户设置并选择 `Create User`
10. 通过下载 CSV 或将密钥复制粘贴到某处，保存为该用户生成的密钥，以便稍后使用。此密钥无法再次获取，请妥善保管。如需重新生成密钥，只需返回上面的步骤 5。

现在，您已具备将 Wasabi 账户添加到 PlaidCloud 文档所需的全部信息。



## PlaidCloud 文档设置

1. 登录 PlaidCloud
2. 选择新文档账户所在的工作区
3. 转到 `Document > Manage Accounts`
4. 选择 `+ New Account` 按钮
5. 选择 `Wasabi Hot Storage` 作为服务类型
6. 填写名称和说明
7. 在**起始路径**字段中输入存储桶名称和可选的路径前缀（例如 `my-bucket` 或 `my-bucket/data`）。第一个路径段是存储桶名称。
8. 根据使用场景选择合适的**安全模型**。不确定时保留 `Private`。
9. 在身份验证凭据下，将上面步骤 10 中创建的 **Access Key** 粘贴到访问密钥 ID 字段
10. 在身份验证凭据下，将上面步骤 10 中创建的 **Secret Key** 粘贴到机密访问密钥字段
11. 如果 Wasabi 账户使用特定区域，请输入**区域**；否则留空
12. 选择“保存”按钮，新的文档账户即可使用
