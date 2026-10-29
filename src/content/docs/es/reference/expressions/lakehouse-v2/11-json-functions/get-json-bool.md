---
title: GET_JSON_BOOL (Lakehouse v2)
description: GET_JSON_BOOL — extrae un valor booleano de un objeto JSON mediante una ruta específica.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/get-json-bool.md
---

Extrae un valor booleano de un objeto JSON mediante una ruta específica.

## Sintaxis de Analyze

```python
func.get_json_bool(get_column(table, 'data'), '$.active')
```

## Ejemplos de Analyze

```python
func.get_json_bool(get_column(table, 'data'), '$.active')

┌───┐
│ 1 │
└───┘
```

## Sintaxis de SQL

```sql
GET_JSON_BOOL(<data>, '$.active')
```

## Ejemplos de SQL

```sql
SELECT GET_JSON_BOOL('{"active": true}', '$.active');

┌───┐
│ 1 │
└───┘
```
