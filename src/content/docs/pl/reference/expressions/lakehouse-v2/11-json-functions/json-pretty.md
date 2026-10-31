---
title: JSON_PRETTY (Lakehouse v2)
description: JSON_PRETTY — formatuje wartość JSON z wcięciami, aby ułatwić jej odczyt.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-pretty.md
---

Formatuje wartość JSON z wcięciami, aby ułatwić jej odczyt.

## Składnia Analyze

```python
func.json_pretty(get_column(table, 'data'))
```

## Przykłady Analyze

```python
func.json_pretty(get_column(table, 'data'))

┌──────────────────┐
│ (formatted JSON) │
└──────────────────┘
```

## Składnia SQL

```sql
JSON_PRETTY(<data>)
```

## Przykłady SQL

```sql
SELECT JSON_PRETTY(PARSE_JSON('{"name":"Alice","age":30}'));

┌────────────────────────────────────┐
│ {
  "name": "Alice",
  "age": 30
} │
└────────────────────────────────────┘
```
