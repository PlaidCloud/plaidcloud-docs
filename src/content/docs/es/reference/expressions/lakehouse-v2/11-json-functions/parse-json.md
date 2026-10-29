---
title: PARSE_JSON (Lakehouse v2)
description: PARSE_JSON — analiza una cadena JSON y devuelve un valor JSON.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/parse-json.md
---

Analiza una cadena JSON y devuelve un valor JSON.

## Sintaxis de Analyze

```python
func.parse_json('{"a":1}')
```

## Ejemplos de Analyze

```python
func.parse_json('{"a": 1}')

┌─────────────┐
│ JSON object │
└─────────────┘
```

## Sintaxis de SQL

```sql
PARSE_JSON('{"a":1}')
```

## Ejemplos de SQL

```sql
SELECT PARSE_JSON('{"name": "Alice"}');

┌──────────────────┐
│ {"name":"Alice"} │
└──────────────────┘
```
