---
title: PARSE_JSON (Lakehouse v2)
description: PARSE_JSON — analisa uma string JSON e retorna um valor JSON.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/parse-json.md
---

Analisa uma string JSON e retorna um valor JSON.

## Sintaxe do Analyze

```python
func.parse_json('{"a":1}')
```

## Exemplos do Analyze

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

## Exemplos de SQL

```sql
SELECT PARSE_JSON('{"name": "Alice"}');

┌──────────────────┐
│ {"name":"Alice"} │
└──────────────────┘
```
