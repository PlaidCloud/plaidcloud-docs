---
title: IGNORE (Lakehouse v1)
description: IGNORE — avec l'instruction insert ignore, les lignes contenant des données non valides qui provoquent l'erreur sont ignorées.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/20-other-functions/ignore.md
---

Avec l'instruction insert ignore, les lignes contenant des données non valides qui provoquent l'erreur sont ignorées, et les lignes contenant des données valides sont insérées dans la table.

## Syntaxe SQL

```sql
INSERT ignore INTO TABLE(column_list)
VALUES( value_list),
      ( value_list),
      ...
```
