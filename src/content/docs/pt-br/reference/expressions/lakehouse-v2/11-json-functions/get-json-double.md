---
title: GET_JSON_DOUBLE (Lakehouse v2)
description: GET_JSON_DOUBLE — extrai um valor double de um objeto JSON por meio de um caminho especificado.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/get-json-double.md
---

Extrai um valor double de um objeto JSON por meio de um caminho especificado.

## Sintaxe do Analyze

```python
func.get_json_double(get_column(table, 'data'), '$.price')
```

## Exemplos do Analyze

```python
func.get_json_double(get_column(table, 'data'), '$.price')

┌───────┐
│ 19.99 │
└───────┘
```

## Sintaxe SQL

```sql
GET_JSON_DOUBLE(<data>, '$.price')
```

## Exemplos de SQL

```sql
SELECT GET_JSON_DOUBLE('{"price": 19.99}', '$.price');

┌───────┐
│ 19.99 │
└───────┘
```
