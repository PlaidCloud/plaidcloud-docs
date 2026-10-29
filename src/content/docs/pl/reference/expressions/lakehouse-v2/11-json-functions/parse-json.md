---
title: PARSE_JSON (Lakehouse v2)
description: PARSE_JSON — analizuje ciąg znaków JSON i zwraca wartość JSON.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/parse-json.md
---

Analizuje ciąg znaków JSON i zwraca wartość JSON.

## Składnia Analyze

```python
func.parse_json('{"a":1}')
```

## Przykłady Analyze

```python
func.parse_json('{"a": 1}')

┌─────────────┐
│ JSON object │
└─────────────┘
```

## Składnia SQL

```sql
PARSE_JSON('{"a":1}')
```

## Przykłady SQL

```sql
SELECT PARSE_JSON('{"name": "Alice"}');

┌──────────────────┐
│ {"name":"Alice"} │
└──────────────────┘
```
