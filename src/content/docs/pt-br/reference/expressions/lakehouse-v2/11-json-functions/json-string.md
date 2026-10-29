---
title: JSON_STRING (Lakehouse v2)
description: JSON_STRING — converte um valor JSON em uma string codificada em JSON.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-string.md
---

Converte um valor JSON em uma string codificada em JSON.

## Sintaxe do Analyze

```python
func.json_string(get_column(table, 'data'))
```

## Exemplos do Analyze

```python
func.json_string(get_column(table, 'json_val'))

┌───────────┐
│ '{"a":1}' │
└───────────┘
```

## Sintaxe SQL

```sql
JSON_STRING(<data>)
```

## Exemplos de SQL

```sql
SELECT JSON_STRING(PARSE_JSON('{"a": 1}'));

┌─────────┐
│ {"a":1} │
└─────────┘
```
