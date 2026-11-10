---
title: 在文档账户中使用起始路径
description: 在 PlaidCloud 文档账户中配置起始路径，以控制浏览文件存储时的默认目录位置。
sidebar:
  order: 5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/account-management/using-start-paths-in-document-accounts.md
---

账户管理表单允许配置存储连接信息和起始路径。起始路径让使用该账户的人从目录树中更深的层级开始浏览目录结构。如果有多个团队需要彼此隔离的文件存储，但只想使用一个底层存储服务账户，此选项尤其有用。



文档账户中的起始路径选项在以下情况下很有用：


* 为特定团队和组控制对子目录的访问
* 仅授予对一个存储桶的访问权限

例如，为 `Team 1` 文档账户设置起始路径 *teams/team_1/*，为 `Team 2` 文档账户设置 *teams/team_2*，即可在共享账户上提供不同的起点。成员打开 Team 1 文档账户时，将从 *team/team_1* 内部开始文件导航。他们无法向上移动到目录树的更高层级，也看不到 *teams/team_1* 之上的任何内容。



Team 2 也有类似的限制，无法导航到 Team 1 的区域。



这样就可以将特定团队限制在目录树的较低层级，同时允许其他团队访问更高层级，而不需要额外的存储桶或特殊权限等任何额外的云存储复杂性。



## 添加和更新起始路径


1. 转到 `Document > Manage`
2. 打开要编辑的账户，然后选择**编辑**
3. 在“起始路径”文本字段中添加起始路径
4. 选择“保存”按钮

## 起始路径格式


路径始终以存储桶名称开头，后跟子目录。



```text
<my-bucket>/folder1/folder2/
```
