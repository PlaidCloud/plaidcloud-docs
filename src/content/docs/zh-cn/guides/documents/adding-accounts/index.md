---
title: 添加新的文档账户
description: 将云端和本地部署的文档存储连接到 PlaidCloud，包括 S3、GCS、Azure Blob、Google Drive、OneDrive、SFTP、WebDAV 等。
sidebar:
  label: 添加新的文档账户
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/index.md
---

将云端和本地部署的文档存储连接到 PlaidCloud，包括 S3、Google Cloud Storage、Azure Blob、Google Drive、OneDrive、SFTP、WebDAV 等。每个提供商都有各自的凭据和连接流程。

最快捷的选择是 **PlaidCloud 托管存储桶**：由 PlaidCloud 为您设置并运行存储，您只需选择一个名称，无需配置其他任何内容。要连接您自己的存储，请在下方选择对应的提供商。

## 已保存的机密为只写

账户的机密（标记为**私钥/密码**的字段，或视账户类型而定的**机密访问密钥**、**账户密钥**、**客户端密钥**、**访问令牌**、**密码**、**系统用户 JSON 密钥**或 **OAuth2 凭据 JSON**）为只写，SFTP 账户的 **RSA 私钥**也是如此。保存之后，它们不会再显示在表单、API 中，也不会显示给 AI 助手。编辑账户时，该字段为空，并提示 *Paste the value; leave blank on edit to keep the saved one.* 留空即可保留已保存的机密，或粘贴新值进行替换。

更改账户的连接位置需要重新输入其机密。如果更改了**起始路径**的第一部分（对于云存储，即存储桶或容器）、SFTP 账户的**主机或 IP 地址**或 **SSH 连接端口**，或者 OneDrive 账户的 **OneDrive 租户 ID**，也需要粘贴机密，否则保存会被拒绝，并提示 *Changing where the account connects needs its secret entered again*。这可以防止能够编辑账户但从未见过其机密的人，把该机密发送到自己选择的服务器。

通过 PlaidCloud MCP 连接器连接的 AI 助手也可以创建和更新账户，包括存储类型、凭据和起始路径。凭据为只写，读取账户时会被隐藏。有关完整示例，请参阅[添加 OneDrive / SharePoint 账户](/zh-cn/guides/documents/adding-accounts/add-onedrive-account/#使用-ai-助手创建账户)。
