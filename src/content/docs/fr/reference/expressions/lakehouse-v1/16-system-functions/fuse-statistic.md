---
title: FUSE_STATISTIC (Lakehouse v1)
description: FUSE_STATISTIC — renvoie le nombre estimé de valeurs distinctes de chaque colonne d'une table.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/16-system-functions/fuse-statistic.md
---

Renvoie le nombre estimé de valeurs distinctes de chaque colonne d'une table.


## Syntaxe SQL

```sql
FUSE_STATISTIC('<database_name>', '<table_name>')
```

## Exemples SQL

Vous utiliserez le plus souvent cette fonction avec `ANALYZE TABLE <table_name>` pour générer et consulter les informations statistiques d'une table. Pour plus d'explications et d'exemples, consultez OPTIMIZE TABLE.
