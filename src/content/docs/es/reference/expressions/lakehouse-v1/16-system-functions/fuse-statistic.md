---
title: FUSE_STATISTIC (Lakehouse v1)
description: FUSE_STATISTIC devuelve el número estimado de valores distintos de cada columna de una tabla.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/16-system-functions/fuse-statistic.md
---

Devuelve el número estimado de valores distintos de cada columna de una tabla.


## Sintaxis de SQL

```sql
FUSE_STATISTIC('<database_name>', '<table_name>')
```

## Ejemplos de SQL

Lo más probable es que use esta función junto con `ANALYZE TABLE <table_name>` para generar y consultar la información estadística de una tabla. Para obtener más explicaciones y ejemplos, consulte OPTIMIZE TABLE.
