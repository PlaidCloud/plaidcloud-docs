---
title: COLUMN_SIZE (Lakehouse v2)
description: COLUMN_SIZE renvoie la taille en octets d'une valeur de colonne sous sa forme sérialisée.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/column-size.md
---

Renvoie la taille en octets d'une valeur de colonne sous sa forme sérialisée.

## Syntaxe Analyze

```python
func.column_size(get_column(table, 'name'))
```

## Exemples Analyze

```python
func.column_size(get_column(table, 'name'))

┌───┐
│ 5 │
└───┘
```

## Syntaxe SQL

```sql
COLUMN_SIZE(<expr>)
```

## Exemples SQL

```sql
SELECT name, COLUMN_SIZE(name) FROM users LIMIT 3;

┌──────���┬───────────────────┐
│ name  │ column_size(name) │
├───────┼───────────────────┤
│ Alice │                 5 │
│ Bob   │                 3 │
│ Eve   │                 3 │
└───────┴───────────────────┘
```
