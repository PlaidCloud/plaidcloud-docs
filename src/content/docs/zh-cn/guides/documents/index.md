---
title: 文件管理
description: 在 PlaidCloud 中管理文件存储账户，以便通过 CSV、Excel、Parquet 及其他文件格式导入和导出数据。
sidebar:
  label: 概览
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/index.md
---

PlaidCloud 文档：在数据和工作流旁边存储、组织、搜索和共享文件。文档可以来自任何已连接的存储账户，并可在工作流中引用。

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 680 200" role="img" aria-label="S3、Google Cloud Storage 和 OneDrive 等已连接的存储账户向 PlaidCloud 文档提供文件，文件在其中进行存储、组织、搜索和共享。随后，工作流步骤引用这些文件来导入和导出数据。" style="width:100%;max-width:680px;height:auto;">
  <defs><marker id="dc-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <text x="76" y="30" text-anchor="middle" font-size="11" font-weight="700" fill="var(--sl-color-gray-3)">存储账户</text>
  <rect x="16" y="40" width="120" height="30" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="76" y="60" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">S3</text>
  <rect x="16" y="82" width="120" height="30" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="76" y="102" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Cloud Storage</text>
  <rect x="16" y="124" width="120" height="30" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="76" y="144" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">OneDrive</text>
  <path d="M136 55 C186 55 206 92 246 96" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#dc-arrow)" />
  <path d="M136 97 L246 100" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#dc-arrow)" />
  <path d="M136 139 C186 139 206 108 246 104" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#dc-arrow)" />
  <rect x="248" y="70" width="180" height="64" rx="10" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="338" y="96" text-anchor="middle" font-size="13" font-weight="700" fill="var(--sl-color-text)">文档</text>
  <text x="338" y="115" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">存储 · 组织 · 搜索 · 共享</text>
  <path d="M428 102 L510 102" stroke="var(--sl-color-gray-3)" stroke-width="1.8" fill="none" marker-end="url(#dc-arrow)" />
  <rect x="512" y="76" width="152" height="52" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="588" y="100" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">工作流步骤</text>
  <text x="588" y="118" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">导入 · 导出文件</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">文件从任何已连接的存储账户进入文档，您可以在其中存储、组织、搜索和共享这些文件，然后在工作流步骤中引用它们来导入和导出数据。</figcaption>
</figure>

## 文档工作区

**文档**打开时，左侧是侧栏，旁边是所选页面。侧栏将页面分组在**文档**（**概览**和**浏览**）和**账户**（**您的账户**和**管理**）下。无法打开某个页面的成员看不到该页面对应的项目。每个页面顶部都有标题和简短的副标题，其操作位于旁边的页眉中。

| 侧栏项目 | 显示内容 |
|---|---|
| **概览** | 您的账户图块（**账户**、**已共享**、**对您私有**、**托管存储桶**、**外部服务**，以及在账户需要关注时显示的**已禁用**）、**已固定**文件、**按服务划分的账户**和**谁可以使用**。选择已固定的文件，会在其所在文件夹处打开**浏览**，并选中该文件。 |
| **浏览** | 文件资源管理器。它会打开您收藏的账户（即您固定了其顶层文件夹的账户）或工作区的默认账户，您可以从页眉中的列表选择其他账户。请参阅[使用文档账户](/zh-cn/guides/documents/using-document/)。 |
| **您的账户** | 您可以使用的所有账户，集中在一个列表中。每行上的**已共享**或**私有**标签表明该账户是与您共享的还是仅属于您。双击某一行可浏览该账户。 |
| **管理** | 您拥有的账户，包含**名称**、**服务**、**安全类型**、**状态**和**说明**。工作区管理员可以在此看到每个文档账户，并可以管理其在其他情况下有权管理的任何账户；系统管理的账户会被拒绝，托管存储桶账户无法克隆。 |

侧栏会在**您的账户**和**管理**旁边显示计数。对于持有并非自己拥有的账户的工作区管理员，**管理**会显示**管理员**而不是计数。概览中有**浏览文件**和**新建账户**按钮，方便快速开始。

### “管理”中的行操作

打开某一行的 **⋯** 菜单，右键单击该行，或使用工具栏的**操作**菜单，可进行以下操作：

- **打开**和**编辑**，用于打开账户页面。
- **克隆…**、**版本历史记录**和**使用位置…**。请参阅[使用位置与重新指向](/zh-cn/guides/documents/account-management/document-account-used-by/)。
- **谁可以使用**，包含**成员**、**组**、**代理**和**所有者**。请参阅[控制文档账户访问](/zh-cn/guides/documents/account-management/control-document-account-access/)。
- **启用**或**禁用**，以及**删除**。

### 账户页面

**新建账户**、**打开**和**编辑**会将账户显示为页面，顶部的**管理账户**用于返回。页面包含以下卡片：

- **常规**：账户的名称、服务、存储桶和起始路径。
- **访问**：安全模型以及谁可以使用该账户。**成员**、**组**、**代理**和**所有者**各有一个**编辑**链接，打开与行菜单相同的选取器。
- **凭据**：所选服务的只写字段。**Credentials saved** 提示表明凭据已设置，已保存的值绝不会显示。将字段留空可保留已保存的内容。SFTP 账户还有**测试连接**。
- **SSH**：仅适用于 SFTP 账户的密钥设置。

页眉中有**浏览**、**使用位置**以及**操作**菜单，其中包含**克隆**、**版本历史记录**、**启用**或**禁用**以及**删除**。如果离开存在未保存更改的页面，PlaidCloud 会询问是否放弃这些更改。

指向文档屏幕的旧链接和书签仍会打开对应的页面。
