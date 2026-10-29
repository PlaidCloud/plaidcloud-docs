---
title: FUSE_STATISTIC (Lakehouse v1)
description: FUSE_STATISTIC：返回表中每一列的不同值估计数量。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/16-system-functions/fuse-statistic.md
---

返回表中每一列的不同值估计数量。


## SQL 语法

```sql
FUSE_STATISTIC('<database_name>', '<table_name>')
```

## SQL 示例

此函数最常与 `ANALYZE TABLE <table_name>` 配合使用，以生成并检查表的统计信息。更多说明和示例，请参阅 OPTIMIZE TABLE。
