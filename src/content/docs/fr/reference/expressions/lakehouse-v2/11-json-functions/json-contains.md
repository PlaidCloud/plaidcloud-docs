---
title: JSON_CONTAINS (Lakehouse v2)
description: JSON_CONTAINS — vérifie si un document JSON contient une valeur donnée à un chemin.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-contains.md
---

Vérifie si un document JSON contient une valeur donnée à un chemin.

## Syntaxe Analyze

```python
func.json_contains(get_column(table, 'data'), '"Alice"', '$.name')
```

## Exemples Analyze

```python
func.json_contains(get_column(table, 'data'), '"Alice"', '$.name')

┌───┐
│ 1 │
└───┘
```

## Syntaxe SQL

```sql
JSON_CONTAINS(<data>, '"Alice"', '$.name')
```

## Exemples SQL

```sql
SELECT JSON_CONTAINS('{"name":"Alice"}', '"Alice"', '$.name');

┌───┐
│ 1 │
└───┘
```
