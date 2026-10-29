---
title: PARSE_JSON (Lakehouse v2)
description: PARSE_JSON – parst eine JSON-Zeichenfolge und gibt einen JSON-Wert zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/parse-json.md
---

Parst eine JSON-Zeichenfolge und gibt einen JSON-Wert zurück.

## Analyze-Syntax

```python
func.parse_json('{"a":1}')
```

## Analyze-Beispiele

```python
func.parse_json('{"a": 1}')

┌─────────────┐
│ JSON object │
└─────────────┘
```

## SQL-Syntax

```sql
PARSE_JSON('{"a":1}')
```

## SQL-Beispiele

```sql
SELECT PARSE_JSON('{"name": "Alice"}');

┌──────────────────┐
│ {"name":"Alice"} │
└──────────────────┘
```
