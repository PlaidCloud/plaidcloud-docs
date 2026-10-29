---
title: GET_JSON_INT (Lakehouse v2)
description: GET_JSON_INT — extrai um valor inteiro de um objeto JSON através de um caminho especificado.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/get-json-int.md
---

Extrai um valor inteiro de um objeto JSON através de um caminho especificado.

## Sintaxe de Analyze

```python
func.get_json_int(get_column(table, 'data'), '$.age')
```

## Exemplos de Analyze

```python
func.get_json_int(get_column(table, 'data'), '$.age')

┌────┐
│ 30 │
└────┘
```

## Sintaxe SQL

```sql
GET_JSON_INT(<data>, '$.age')
```

## Exemplos SQL

```sql
SELECT GET_JSON_INT('{"age": 30}', '$.age');

┌────┐
│ 30 │
└────┘
```
