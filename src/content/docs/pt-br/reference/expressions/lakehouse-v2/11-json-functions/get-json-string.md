---
title: GET_JSON_STRING (Lakehouse v2)
description: GET_JSON_STRING — extrai um valor de string de um objeto JSON por meio de um caminho especificado.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/get-json-string.md
---

Extrai um valor de string de um objeto JSON por meio de um caminho especificado.

## Sintaxe do Analyze

```python
func.get_json_string(get_column(table, 'data'), '$.name')
```

## Exemplos do Analyze

```python
func.get_json_string(get_column(table, 'data'), '$.name')

┌───────┐
│ Alice │
└───────┘
```

## Sintaxe SQL

```sql
GET_JSON_STRING(<data>, '$.name')
```

## Exemplos de SQL

```sql
SELECT GET_JSON_STRING('{"name": "Alice"}', '$.name');

┌───────┐
│ Alice │
└───────┘
```
