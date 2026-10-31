---
title: JSON_PRETTY (Lakehouse v2)
description: JSON_PRETTY — formata um valor JSON com indentação para melhorar a legibilidade.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-pretty.md
---

Formata um valor JSON com indentação para melhorar a legibilidade.

## Sintaxe de Analyze

```python
func.json_pretty(get_column(table, 'data'))
```

## Exemplos de Analyze

```python
func.json_pretty(get_column(table, 'data'))

┌──────────────────┐
│ (formatted JSON) │
└──────────────────┘
```

## Sintaxe SQL

```sql
JSON_PRETTY(<data>)
```

## Exemplos SQL

```sql
SELECT JSON_PRETTY(PARSE_JSON('{"name":"Alice","age":30}'));

┌────────────────────────────────────┐
│ {
  "name": "Alice",
  "age": 30
} │
└────────────────────────────────────┘
```
