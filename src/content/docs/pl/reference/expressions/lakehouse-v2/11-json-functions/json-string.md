---
title: JSON_STRING (Lakehouse v2)
description: JSON_STRING — konwertuje wartość JSON na ciąg znaków zakodowany w formacie JSON.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-string.md
---

Konwertuje wartość JSON na ciąg znaków zakodowany w formacie JSON.

## Składnia Analyze

```python
func.json_string(get_column(table, 'data'))
```

## Przykłady Analyze

```python
func.json_string(get_column(table, 'json_val'))

┌───────────┐
│ '{"a":1}' │
└───────────┘
```

## Składnia SQL

```sql
JSON_STRING(<data>)
```

## Przykłady SQL

```sql
SELECT JSON_STRING(PARSE_JSON('{"a": 1}'));

┌─────────┐
│ {"a":1} │
└─────────┘
```
