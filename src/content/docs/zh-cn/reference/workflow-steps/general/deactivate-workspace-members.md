---
title: Deactivate Workspace Members 步骤
description: 停用项目表中列出的工作区成员，按电子邮件地址或用户名匹配。
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/deactivate-workspace-members.md
---

import { Aside } from '@astrojs/starlight/components';

## 说明

停用源表中指定的工作区成员。可用于根据权威名单（如 HR 提取或访问审查）自动执行离职处理，而无需手动逐个停用。

可与 [Get Workspace Members](/zh-cn/reference/workflow-steps/general/get-workspace-members/) 配合使用，生成不应再拥有访问权限的人员名单。

<Aside type="caution" title="此操作会撤销访问权限">
  步骤运行时，每个匹配到的成员都会失去访问权限。计划运行此步骤之前，请检查源表只包含您要处理的人员。
</Aside>

## 名单中的工作区管理员

[只有工作区管理员才能停用工作区管理员](/zh-cn/administration/access/member-management/#更改工作区管理员)。如果步骤在没有工作区管理员权限的情况下运行，且名单中包含管理员，它会保持这些管理员为活动状态，停用其他所有人，然后以错误结束，错误消息会给出已停用的成员数量，并列出每个被保留为活动状态的管理员。已停用的成员保持停用状态。要停用管理员，请由工作区管理员在 Identity 中操作。

## 配置

### 成员搜索参数

源表中的行与成员的匹配方式。请选择其一：

- **电子邮件**（默认）
- **用户名**

## 相关内容

- [常规步骤](/zh-cn/reference/workflow-steps/general/)
- [Get Workspace Members](/zh-cn/reference/workflow-steps/general/get-workspace-members/)
- [成员管理](/zh-cn/administration/access/)
