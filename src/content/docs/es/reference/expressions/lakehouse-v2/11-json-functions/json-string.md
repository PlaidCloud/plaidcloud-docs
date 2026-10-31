---
title: JSON_STRING (Lakehouse v2)
description: JSON_STRING — convierte un valor JSON en una cadena codificada como JSON.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-string.md
---

Convierte un valor JSON en una cadena codificada como JSON.

## Sintaxis de Analyze

```python
func.json_string(get_column(table, 'data'))
```

## Ejemplos de Analyze

```python
func.json_string(get_column(table, 'json_val'))

┌───────────┐
│ '{"a":1}' │
└───────────┘
```

## Sintaxis de SQL

```sql
JSON_STRING(<data>)
```

## Ejemplos de SQL

```sql
SELECT JSON_STRING(PARSE_JSON('{"a": 1}'));

┌─────────┐
│ {"a":1} │
└─────────┘
```
