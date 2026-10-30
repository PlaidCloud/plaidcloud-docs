---
title: GET_JSON_OBJECT (Lakehouse v2)
description: GET_JSON_OBJECT — extrai um objeto JSON de uma string JSON por meio de um caminho especificado.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/get-json-object.md
---

Extrai um objeto JSON de uma string JSON por meio de um caminho especificado.

## Sintaxe do Analyze

```python
func.get_json_object(get_column(table, 'data'), '$.address')
```

## Exemplos do Analyze

```python
func.get_json_object(get_column(table, 'data'), '$.address')

┌─────────────┐
│ JSON object │
└─────────────┘
```

## Sintaxe SQL

```sql
GET_JSON_OBJECT(<data>, '$.address')
```

## Exemplos de SQL

```sql
SELECT GET_JSON_OBJECT('{"address":{"city":"NYC"}}', '$.address');

┌────────────────┐
│ {"city":"NYC"} │
└────────────────┘
```
