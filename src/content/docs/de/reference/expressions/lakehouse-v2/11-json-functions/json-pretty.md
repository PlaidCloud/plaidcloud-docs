---
title: JSON_PRETTY (Lakehouse v2)
description: JSON_PRETTY – formatiert einen JSON-Wert zur besseren Lesbarkeit mit Einrückung.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-pretty.md
---

Formatiert einen JSON-Wert zur besseren Lesbarkeit mit Einrückung.

## Analyze-Syntax

```python
func.json_pretty(get_column(table, 'data'))
```

## Analyze-Beispiele

```python
func.json_pretty(get_column(table, 'data'))

┌──────────────────┐
│ (formatted JSON) │
└──────────────────┘
```

## SQL-Syntax

```sql
JSON_PRETTY(<data>)
```

## SQL-Beispiele

```sql
SELECT JSON_PRETTY(PARSE_JSON('{"name":"Alice","age":30}'));

┌────────────────────────────────────┐
│ {
  "name": "Alice",
  "age": 30
} │
└────────────────────────────────────┘
```
