---
title: JSON_QUERY (Lakehouse v2)
description: JSON_QUERY — extrait une valeur JSON d'un document JSON à l'aide d'une expression de chemin.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-query.md
---

Extrait une valeur JSON d'un document JSON à l'aide d'une expression de chemin.

## Syntaxe Analyze

```python
func.json_query(get_column(table, 'data'), '$.items')
```

## Exemples Analyze

```python
func.json_query(get_column(table, 'data'), '$.items')

┌────────────┐
│ JSON value │
└────────────┘
```

## Syntaxe SQL

```sql
JSON_QUERY(<data>, '$.items')
```

## Exemples SQL

```sql
SELECT JSON_QUERY(PARSE_JSON('{"items":[1,2,3]}'), '$.items');

┌─────────┐
│ [1,2,3] │
└─────────┘
```
