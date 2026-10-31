---
title: PARSE_JSON (Lakehouse v2)
description: PARSE_JSON — analisa uma cadeia de caracteres JSON e devolve um valor JSON.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/parse-json.md
---

Analisa uma cadeia de caracteres JSON e devolve um valor JSON.

## Sintaxe de Analyze

```python
func.parse_json('{"a":1}')
```

## Exemplos de Analyze

```python
func.parse_json('{"a": 1}')

┌─────────────┐
│ JSON object │
└─────────────┘
```

## Sintaxe SQL

```sql
PARSE_JSON('{"a":1}')
```

## Exemplos SQL

```sql
SELECT PARSE_JSON('{"name": "Alice"}');

┌──────────────────┐
│ {"name":"Alice"} │
└──────────────────┘
```
