---
title: Delete Old Files 步骤
description: 删除文档账户中早于或晚于所选时长的文件，并在删除任何内容之前提供试运行列表。
sidebar:
  order: 23
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/document-delete-old-files.md
---

import { Aside } from '@astrojs/starlight/components';

## 说明

根据时长删除文档账户中的文件。可用于防止导出或落地文件夹无限增长，例如删除昨天的提取文件，或清除一年前的归档。

## 配置

### 要删除的文件

- **文件路径** — 要处理的文档账户和文件夹。
- **时长** — 一个数字加一个单位：分钟、小时、天、月或年。
- **早于或晚于** — 删除最后修改时间**早于**截止时间的文件（通常的清理方向），或**晚于**截止时间的文件。
- **递归** — 默认关闭。开启后包括子文件夹。
- **测试结果表** — 步骤编辑器的**测试**按钮将匹配文件的预览写入的表。

<Aside type="caution" title="请用测试预览，而不是运行步骤">
  预览来自编辑步骤时的**测试**按钮。
  在工作流中运行该步骤始终会执行删除 — 没有试运行模式，
  测试结果表也不会使其改为预览。删除不可逆，
  且在开启**递归**时路径有误，影响范围会比预期更大，因此
  在设置计划之前请先检查预览。
</Aside>

## 相关内容

- [文档步骤](/zh-cn/reference/workflow-steps/document/)
- [Delete Document File 步骤](/zh-cn/reference/workflow-steps/document/delete-document-file/)
- [目录列表](/zh-cn/reference/workflow-steps/document/directory-listing/)
