---
title: 添加 Google Drive 账户
description: 将 Google Drive 存储账户添加到 PlaidCloud，以使用 Google Drive 云存储导入和导出数据文件。
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-google-drive-account.md
---

## Google Drive 设置

以下步骤需要在 Google Cloud Console 中完成，以创建 PlaidCloud 可用于访问 Google Drive 的服务账户。

### 创建 Google Cloud 项目

1. 登录 [Google Cloud Console](https://console.cloud.google.com)
2. 创建新项目或选择现有项目

### 启用 Google Drive API

1. 导航到 **APIs & Services > Library**
2. 搜索 **Google Drive API**
3. 选择它并点击 **Enable**

### 创建服务账户

1. 导航到 **APIs & Services > Credentials**
2. 选择 **+ Create Credentials > Service account**
3. 输入服务账户的名称（例如 `plaidcloud-drive`）
4. 选择 **Create and Continue**
5. 可选择授予角色（例如只读用 **Viewer**，读写用 **Editor**）。选择 **Continue**。
6. 选择 **Done**

### 生成服务账户密钥

1. 在 **Service Accounts** 列表中，选择刚创建的服务账户
2. 导航到 **Keys** 选项卡
3. 选择 **Add Key > Create new key**
4. 选择 **JSON** 格式并选择 **Create**
5. 将下载一个 JSON 密钥文件。请妥善保存该文件，其中包含 PlaidCloud 将使用的凭据。

### 与服务账户共享 Drive 内容

1. 复制服务账户的电子邮件地址（例如 `plaidcloud-drive@your-project.iam.gserviceaccount.com`）
2. 在 Google Drive 中，将希望 PlaidCloud 访问的文件夹与该电子邮件地址共享，并授予 **Editor** 访问权限

现在，您应该已具备将 Google Drive 账户添加到 PlaidCloud 文档所需的一切。


## PlaidCloud 文档设置

1. 登录 PlaidCloud
2. 选择新文档账户所在的工作区
3. 转到 `Document > Manage Accounts`
4. 选择 `+ New Account` 按钮
5. 选择 `Google Drive` 作为服务类型
6. 填写名称和说明
7. 在 **起始路径** 字段中输入共享文件夹路径，或留空以访问所有共享内容
8. 根据您的使用场景选择合适的 **安全模型**。如果不确定，请保持为 `Private`。
9. 将 JSON 密钥文件的全部内容粘贴到“身份验证凭据”下的“OAuth2 凭据 JSON”字段中
10. 选择“保存”按钮，您的新文档账户即可使用
