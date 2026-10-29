---
title: JSON_REMOVE (Lakehouse v2)
description: JSON_REMOVE — supprime un élément d'un document JSON au chemin spécifié.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-remove.md
---

Supprime un élément d'un document JSON au chemin spécifié.

## Syntaxe Analyze

```python
func.json_remove(get_column(table, 'data'), '$.temp')
```

## Exemples Analyze

```python
func.json_remove(get_column(table, 'data'), '$.temp')

┌──────────────────────┐
│ JSON without element │
└──────────────────────┘
```

## Syntaxe SQL

```sql
JSON_REMOVE(<data>, '$.temp')
```

## Exemples SQL

```sql
SELECT JSON_REMOVE(PARSE_JSON('{"name":"Alice","temp":1}'), '$.temp');

┌──────────────────┐
│ {"name":"Alice"} │
└──────────────────┘
```
