---
title: IGNORE
---

By using insert ignore statement, the rows with invalid data that cause the error are ignored and the rows with valid data are inserted into the table.

## SQL Syntax

```sql
INSERT ignore INTO TABLE(column_list)
VALUES( value_list),
      ( value_list),
      ...
```
