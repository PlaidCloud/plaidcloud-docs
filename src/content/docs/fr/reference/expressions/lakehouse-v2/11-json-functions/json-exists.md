---
title: JSON_EXISTS (Lakehouse v2)
description: JSON_EXISTS — vérifie si un document JSON contient une valeur au chemin spécifié.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-exists.md
---

Vérifie si un document JSON contient une valeur au chemin spécifié.

## Syntaxe Analyze

```python
func.json_exists(get_column(table, 'data'), '$.name')
```

## Exemples Analyze

```python
func.json_exists(get_column(table, 'data'), '$.name')

┌───┐
│ 1 │
└───┘
```

## Syntaxe SQL

```sql
JSON_EXISTS(<data>, '$.name')
```

## Exemples SQL

```sql
SELECT JSON_EXISTS(PARSE_JSON('{"name":"Alice"}'), '$.name');

┌───┐
│ 1 │
└───┘
```
