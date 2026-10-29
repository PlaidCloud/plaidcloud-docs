---
title: JSON_STRING (Lakehouse v2)
description: JSON_STRING — convertit une valeur JSON en chaîne encodée en JSON.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-string.md
---

Convertit une valeur JSON en chaîne encodée en JSON.

## Syntaxe Analyze

```python
func.json_string(get_column(table, 'data'))
```

## Exemples Analyze

```python
func.json_string(get_column(table, 'json_val'))

┌───────────┐
│ '{"a":1}' │
└───────────┘
```

## Syntaxe SQL

```sql
JSON_STRING(<data>)
```

## Exemples SQL

```sql
SELECT JSON_STRING(PARSE_JSON('{"a": 1}'));

┌─────────┐
│ {"a":1} │
└─────────┘
```
