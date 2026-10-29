---
title: IGNORE (Lakehouse v1)
description: IGNORE hace que, al usar la sentencia insert ignore, se omitan las filas con datos no válidos que causan el error.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/20-other-functions/ignore.md
---

Al usar la sentencia insert ignore, se omiten las filas con datos no válidos que causan el error y las filas con datos válidos se insertan en la tabla.

## Sintaxis de SQL

```sql
INSERT ignore INTO TABLE(column_list)
VALUES( value_list),
      ( value_list),
      ...
```
