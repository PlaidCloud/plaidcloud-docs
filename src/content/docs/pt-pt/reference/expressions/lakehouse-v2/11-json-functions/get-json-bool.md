---
title: GET_JSON_BOOL (Lakehouse v2)
description: GET_JSON_BOOL — extrai um valor booleano de um objeto JSON através de um caminho especificado.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/get-json-bool.md
---

Extrai um valor booleano de um objeto JSON através de um caminho especificado.

## Sintaxe de Analyze

```python
func.get_json_bool(get_column(table, 'data'), '$.active')
```

## Exemplos de Analyze

```python
func.get_json_bool(get_column(table, 'data'), '$.active')

┌───┐
│ 1 │
└───┘
```

## Sintaxe SQL

```sql
GET_JSON_BOOL(<data>, '$.active')
```

## Exemplos SQL

```sql
SELECT GET_JSON_BOOL('{"active": true}', '$.active');

┌───┐
│ 1 │
└───┘
```
