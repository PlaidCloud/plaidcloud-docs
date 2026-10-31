---
title: Table Restore to Timestamp 步骤
description: 作为工作流步骤，将 PlaidCloud 表就地恢复到在某个时间点或之前创建的最新快照。
sidebar:
  order: 45
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/tables/table-restore-timestamp.md
---

## 说明

**表：恢复到时间戳** 会将表就地替换为在某个时间点或之前创建的最新快照。可用它将表回滚到期末时的状态，或回滚到出错的加载之前。恢复会更改表本身，因此读取该表的每个步骤和仪表板看到的都是恢复后的行。

## 恢复到某个时间点

| 设置 | 是否必填 | 作用 |
| --- | --- | --- |
| 表 | 是 | 要恢复的表。 |
| 时间戳 | 是 | 时间点，可以是 ISO-8601 时间（例如 `2026-09-30T23:59:59Z`），也可以是自 1970 年起的秒数。没有时区的时间按 UTC 处理。也可以使用工作流变量，例如 `{restore_time}`。 |
| 恰好在时间戳创建的快照也算 | 否 | 默认开启。清除后，只会恢复到在时间戳之前创建的快照。 |

如果在时间戳或之前没有创建过快照，步骤会在完成时给出警告，保持表不变，工作流继续运行。找不到表时同样会在完成时给出警告。在只保留命名快照的存储引擎上，表只能恢复到恰好在时间戳创建的快照；请在您将来想要返回的时间点创建命名快照。

## 相关内容

- [还原表](/zh-cn/reference/workflow-steps/import/restore-tables/)
- [表步骤](/zh-cn/reference/workflow-steps/tables/)
