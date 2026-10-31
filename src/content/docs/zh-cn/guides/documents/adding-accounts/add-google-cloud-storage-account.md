---
title: 添加 Google Cloud Storage 账户
description: 将 Google Cloud Storage 账户添加到 PlaidCloud，以使用 Google 云对象存储导入和导出数据文件。
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-google-cloud-storage-account.md
---

## Google Cloud 设置


以下步骤需要在 Google Cloud Platform 中完成


1. 登录或创建 Google Cloud Platform 账户
2. 选择或创建 Google Cloud Storage 账户所在的项目
3. 在 Google Cloud Platform 控制台中转到 `Cloud Storage > Browser`
4. 创建默认存储桶或测试存储桶
5. 在 Google Cloud Platform 控制台中转到 `IAM & Admin > Service Accounts`
6. 选择 `+ Create Service Account` 按钮
7. 填写服务账户信息并创建账户
8. 在服务账户列表中找到刚创建的服务账户，然后从右侧的上下文菜单中选择 `Manage Keys`
9. 在 `Add Key` 菜单下，选择 `Create a Key`
10. 出现提示时，为密钥选择 JSON 格式。这将生成密钥并自动下载到您的桌面。您将无法再次检索此密钥，因此请妥善保管。如果需要重新生成密钥，只需返回上面的第 8 步。
11. 在 Google Cloud Platform 控制台中转到 `IAM & Admin > IAM`
12. 找到刚创建的服务账户，然后点击编辑权限图标
13. 为该服务账户添加 `Storage Admin` 和 `Storage Transfer Admin` 权限并保存。请注意，也可以分配权限较低的权限，但这会影响通过文档可用的功能。

现在，您应该已具备将 GCS 账户添加到 PlaidCloud 文档所需的一切。



## PlaidCloud 文档设置

1. 登录 PlaidCloud
2. 选择新文档账户所在的工作区
3. 转到 `Document > Manage Accounts`
4. 选择 `+ New Account` 按钮
5. 选择 `Google Cloud Storage` 作为服务类型
6. 填写名称和说明
7. 在 **起始路径** 字段中输入存储桶名称和可选的路径前缀（例如 `my-bucket` 或 `my-bucket/data`）。第一个路径段是存储桶名称。
8. 根据您的使用场景选择合适的 **安全模型**。如果不确定，请保持为 `Private`。
9. 打开上面第 10 步中下载的服务账户 JSON 密钥文件，并复制全部内容
10. 将内容粘贴到“身份验证凭据”下的 **系统用户 JSON 密钥** 字段中
11. 选择“保存”按钮，您的新文档账户即可使用

需要有效的服务账户密钥。保存账户时如果没有密钥，或者提供的不是 Google 服务账户密钥，系统会拒绝，并提示“GCS document accounts require a valid service-account key.”。已保存但没有有效密钥的现有账户将停止工作，直到您将密钥粘贴到 **系统用户 JSON 密钥** 字段中。
