---
title: JSON_SET (Lakehouse v2)
description: JSON_SET — define um valor em um documento JSON em um caminho especificado.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-set.md
---

Define um valor em um documento JSON em um caminho especificado.

## Sintaxe do Analyze

```python
func.json_set(get_column(table, 'data'), '$.age', 31)
```

## Exemplos do Analyze

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

## Exemplos de SQL

```sql
SELECT JSON_SET(PARSE_JSON('{"name":"Alice"}'), '$.age', 30);

┌───────────────────────────┐
│ {"name":"Alice","age":30} │
└───────────────────────────┘
```
