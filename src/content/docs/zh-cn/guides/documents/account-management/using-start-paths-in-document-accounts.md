---
title: 在文档账户中使用起始路径
description: 在 PlaidCloud 文档账户中配置起始路径，以控制浏览文件存储时的默认目录位置。
sidebar:
  order: 5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/account-management/using-start-paths-in-document-accounts.md
---

账户管理表单允许配置存储连接信息和起始路径。起始路径让使用该账户的人从目录树更深的位置开始浏览目录结构。当多个团队需要隔离的文件存储，而您只想使用一个底层存储服务账户时，此选项非常有用。



文档账户中的起始路径选项在以下情况下很有用：


* 控制特定团队和分组对子目录的访问
* 仅授予对一个存储桶的访问权限

例如，为 `Team 1` 文档账户设置起始路径 *teams/team_1/*，并为 `Team 2` 文档账户设置 *teams/team_2*，即可在共享账户上提供不同的起点。成员打开 Team 1 文档账户时，将从 *team/team_1* 内部开始文件导航。他们无法沿树向上移动，也看不到 *teams/team_1* 之上的任何内容。



Team 2 也有类似的限制，无法导航到 Team 1 的区域。



这样既能将特定团队限制在树的较低层级，又能让其他团队拥有树中更高层级的访问权限，而无需额外的云存储复杂性，例如额外的存储桶或特殊权限。



## 添加和更新起始路径


1. 转到“文档”>“管理账户”
2. 选择要编辑的账户并进入编辑模式
3. 在“起始路径”文本字段中添加起始路径
4. 选择“保存”按钮

## 起始路径格式


路径始终以存储桶名称开头，后跟子目录。



```text
<my-bucket>/folder1/folder2/
```
