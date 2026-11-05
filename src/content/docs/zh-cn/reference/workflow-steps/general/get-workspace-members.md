---
title: Get Workspace Members 步骤
description: 将工作区的成员写入项目表，并可选择要包含的身份和活动字段。
sidebar:
  order: 11
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/get-workspace-members.md
---

## 说明

将工作区的成员写入项目表。可用于报告访问情况、将成员列表与人力资源数据源核对，或根据当前拥有访问权限的人员驱动下游步骤。

## 配置

### 要包含的信息

默认开启：**姓**、**名**、**电子邮件**、**用户名**、**成员创建日期**和**上次登录时间戳**。

### 其他设置

默认关闭：

- **包含已停用的成员** — 将输出范围扩大到活动成员之外。
- **登录历史记录模式** — 返回登录历史记录，而不是仅返回上次登录。

## 安全日志

每次运行都会向安全日志写入一条记录，记录所写入的列、目标表，以及工作流、步骤和运行。

## 相关内容

- [常规步骤](/zh-cn/reference/workflow-steps/general/)
- [Deactivate Workspace Members 步骤](/zh-cn/reference/workflow-steps/general/deactivate-workspace-members/)
- [Get Workspace Usage 步骤](/zh-cn/reference/workflow-steps/general/get-workspace-usage/)
- [成员管理](/zh-cn/administration/access/)
