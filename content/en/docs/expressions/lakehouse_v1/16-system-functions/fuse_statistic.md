---
title: FUSE_STATISTIC
description: "Learn how to use the FUSE_STATISTIC system function in PlaidCloud Lakehouse. Returns the estimated number of distinct values of each column in a table."
---

Returns the estimated number of distinct values of each column in a table.


## SQL Syntax

```sql
FUSE_STATISTIC('<database_name>', '<table_name>')
```

## SQL Examples

You're most likely to use this function together with `ANALYZE TABLE <table_name>` to generate and check the statistical information of a table. For more explanations and examples, see OPTIMIZE TABLE.