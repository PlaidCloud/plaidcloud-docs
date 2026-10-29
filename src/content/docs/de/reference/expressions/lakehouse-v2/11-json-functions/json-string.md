---
title: JSON_STRING (Lakehouse v2)
description: JSON_STRING – wandelt einen JSON-Wert in eine JSON-codierte Zeichenfolge um.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-string.md
---

Wandelt einen JSON-Wert in eine JSON-codierte Zeichenfolge um.

## Analyze-Syntax

```python
func.json_string(get_column(table, 'data'))
```

## Analyze-Beispiele

```python
func.json_string(get_column(table, 'json_val'))

┌───────────┐
│ '{"a":1}' │
└───────────┘
```

## SQL-Syntax

```sql
JSON_STRING(<data>)
```

## SQL-Beispiele

```sql
SELECT JSON_STRING(PARSE_JSON('{"a": 1}'));

┌─────────┐
│ {"a":1} │
└─────────┘
```
