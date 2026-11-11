---
title: 添加 Azure Data Lake Gen2 账户
description: 将 Azure Data Lake Storage Gen2 账户添加到 PlaidCloud，以便使用 Azure 上的分层命名空间存储导入和导出数据文件。
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-azure-data-lake-gen2-account.md
---

## Azure Data Lake Gen2 设置

Azure Data Lake Storage Gen2 构建在启用了分层命名空间的 Azure Blob Storage 之上。这些步骤需要在 Azure 门户中完成。

1. 登录 [Azure 门户](https://portal.azure.com)
2. 导航到 **Storage accounts**，选择或创建一个已启用 **Hierarchical namespace** 的存储账户
3. 在左侧边栏的 **Security + networking** 下，选择 **Access keys**
4. 复制 **Storage account name** 和其中一个 **Key** 值。保存这两项，供下面的 PlaidCloud 文档设置使用。
5. 导航到 **Data storage** 下的 **Containers**，如果还没有文件系统（容器），则创建一个。记下文件系统名称。

现在，您已具备将 Azure Data Lake Gen2 账户添加到 PlaidCloud 文档所需的一切。


## PlaidCloud 文档设置

1. 登录 PlaidCloud
2. 选择新文档账户所在的工作区
3. 转到 `Document > Manage`
4. 选择**新建账户**按钮
5. 选择 `Azure Data Lake Gen2` 作为服务类型
6. 填写名称和描述
7. 在**起始路径**字段中输入文件系统名称和可选的路径前缀（例如 `my-filesystem/data`）。路径的第一段是文件系统名称。
8. 为您的用例选择合适的**安全模型**。如果不确定，请保留为 `Private`。
9. 将 **Storage account name** 粘贴到“身份验证凭据”下的“账户名称”字段中
10. 将 **Key** 粘贴到“身份验证凭据”下的“账户密钥”字段中
11. 选择“保存”按钮，新的文档账户即可投入使用
