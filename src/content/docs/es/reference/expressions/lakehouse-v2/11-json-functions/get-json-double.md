---
title: GET_JSON_DOUBLE (Lakehouse v2)
description: GET_JSON_DOUBLE — extrae un valor de tipo double de un objeto JSON mediante una ruta específica.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/get-json-double.md
---

Extrae un valor de tipo double de un objeto JSON mediante una ruta específica.

## Sintaxis de Analyze

```python
func.get_json_double(get_column(table, 'data'), '$.price')
```

## Ejemplos de Analyze

```python
func.get_json_double(get_column(table, 'data'), '$.price')

┌───────┐
│ 19.99 │
└───────┘
```

## Sintaxis de SQL

```sql
GET_JSON_DOUBLE(<data>, '$.price')
```

## Ejemplos de SQL

```sql
SELECT GET_JSON_DOUBLE('{"price": 19.99}', '$.price');

┌───────┐
│ 19.99 │
└───────┘
```
