---
title: GET_JSON_STRING (Lakehouse v2)
description: GET_JSON_STRING — extrai um valor de cadeia de caracteres de um objeto JSON através de um caminho especificado.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/get-json-string.md
---

Extrai um valor de cadeia de caracteres de um objeto JSON através de um caminho especificado.

## Sintaxe de Analyze

```python
func.get_json_string(get_column(table, 'data'), '$.name')
```

## Exemplos de Analyze

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

## Exemplos SQL

```sql
SELECT GET_JSON_STRING('{"name": "Alice"}', '$.name');

┌───────┐
│ Alice │
└───────┘
```
