---
title: 添加 Google Drive 账户
description: 将 Google Drive 存储账户添加到 PlaidCloud，以使用 Google Drive 云存储导入和导出数据文件。
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-google-drive-account.md
---

## Google Drive 设置

以下步骤需要在 Google Cloud Console 中完成，用于创建 PlaidCloud 访问 Google Drive 所用的服务账户。

### 创建 Google Cloud 项目

1. 登录 [Google Cloud Console](https://console.cloud.google.com)
2. 创建新项目或选择现有项目

### 启用 Google Drive API

1. 导航到 **APIs & Services > Library**
2. 搜索 **Google Drive API**
3. 选择它并点击 **启用**

### 创建服务账户

1. 导航到 **APIs & Services > Credentials**
2. 选择 **+ Create Credentials > Service account**
3. 输入服务账户的名称（例如 `plaidcloud-drive`）
4. 选择 **创建并继续**
5. 可选择授予角色（例如只读授予 **查看者**，读写授予 **编辑器**）。选择 **继续**。
6. 选择 **完成**

### 生成服务账户密钥

1. 在 **Service Accounts** 列表中，选择刚创建的服务账户
2. 导航到 **键** 选项卡
3. 选择 **添加键 > 新建键**
4. 选择 **JSON 格式化** 并选择 **创建**
5. 系统将下载一个 JSON 密钥文件。请妥善保存该文件，其中包含 PlaidCloud 将使用的凭据。

### 与服务账户共享 Drive 内容

1. 复制服务账户的电子邮件地址（例如 `plaidcloud-drive@your-project.iam.gserviceaccount.com`）
2. 在 Google Drive 中，将希望 PlaidCloud 访问的文件夹与该电子邮件地址共享，并授予 **编辑器** 访问权限。若要使用共享云端硬盘，请改为将服务账户添加为其成员。

现在，已具备将 Google Drive 账户添加到 PlaidCloud 文档所需的一切。


## PlaidCloud 文档设置

1. 登录 PlaidCloud
2. 选择新文档账户所在的工作区
3. 转到 `Document > Manage`
4. 选择**新建账户**按钮
5. 选择 `Google Drive` 作为服务类型
6. 填写名称和说明
7. 在**起始路径**字段中输入共享文件夹路径，或留空以访问所有共享内容
8. 根据使用场景选择合适的**安全模型**。如果不确定，请保留 `Private`。
9. 将服务账户 JSON 密钥文件的全部内容粘贴到身份验证凭据下该账户的私钥字段中
10. 选择“保存”按钮，新的文档账户即可使用

## 在工作流中使用该账户

Google Drive 账户既可在文档浏览器中使用，也可在工作流中使用。步骤可以列出、导入、导出、复制、移动、重命名和删除文件，并创建文件夹。

- **地点。** 账户的顶层地点是与服务账户共享的文件夹，以及该服务账户所属的共享云端硬盘。路径为文件夹名称，例如 `Finance/Reports/2026`。如果两个共享文件夹或共享云端硬盘同名，账户将拒绝打开该名称。请重命名或取消共享其中除一个以外的所有项。
- **Google 表格。** Google 表格会以 `.xlsx` 导出的形式读取，并显示为 `Name.xlsx`。其他 Google Workspace 文件（如文档和幻灯片）无法读取。
- **我的云端硬盘中的新文件。** 服务账户没有自己的存储空间，因此在位于某人个人“我的云端硬盘”中的文件夹里，它可以覆盖现有文件，但无法创建新文件。请先在该处创建文件，或使用共享云端硬盘中的文件夹，后者可以接受新文件和文件夹。
- **缺失的文件夹。** 不存在的文件夹会列为空，而不会引发错误。
- **限流。** 当 Google 对请求限流或返回临时错误时，PlaidCloud 会自动重试。
