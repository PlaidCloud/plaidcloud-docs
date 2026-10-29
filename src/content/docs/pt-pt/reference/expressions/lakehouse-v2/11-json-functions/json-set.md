---
title: JSON_SET (Lakehouse v2)
description: JSON_SET — define um valor num documento JSON num caminho especificado.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-set.md
---

Define um valor num documento JSON num caminho especificado.

## Sintaxe de Analyze

```python
func.json_set(get_column(table, 'data'), '$.age', 31)
```

## Exemplos de Analyze

```python
func.json_set(get_column(table, 'data'), '$.age', 31)

┌──────────────┐
│ updated JSON │
└──────────────┘
```

## Sintaxe SQL

```sql
JSON_SET(<data>, '$.age', 31)
```

## Exemplos SQL

```sql
SELECT JSON_SET(PARSE_JSON('{"name":"Alice"}'), '$.age', 30);

┌───────────────────────────┐
│ {"name":"Alice","age":30} │
└───────────────────────────┘
```
