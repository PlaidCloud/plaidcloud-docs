---
title: JSON_PRETTY (Lakehouse v2)
description: JSON_PRETTY — da formato a un valor JSON con sangría para facilitar su lectura.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-pretty.md
---

Da formato a un valor JSON con sangría para facilitar su lectura.

## Sintaxis de Analyze

```python
func.json_pretty(get_column(table, 'data'))
```

## Ejemplos de Analyze

```python
func.json_pretty(get_column(table, 'data'))

┌──────────────────┐
│ (formatted JSON) │
└──────────────────┘
```

## Sintaxis de SQL

```sql
JSON_PRETTY(<data>)
```

## Ejemplos de SQL

```sql
SELECT JSON_PRETTY(PARSE_JSON('{"name":"Alice","age":30}'));

┌────────────────────────────────────┐
│ {
  "name": "Alice",
  "age": 30
} │
└────────────────────────────────────┘
```
