---
title: IGNORE (Lakehouse v1)
description: IGNORE：使用 insert ignore 语句时，会忽略包含导致错误的无效数据的行，并将包含有效数据的行插入表中。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/20-other-functions/ignore.md
---

使用 insert ignore 语句时，会忽略包含导致错误的无效数据的行，并将包含有效数据的行插入表中。

## SQL 语法

```sql
INSERT ignore INTO TABLE(column_list)
VALUES( value_list),
      ( value_list),
      ...
```
