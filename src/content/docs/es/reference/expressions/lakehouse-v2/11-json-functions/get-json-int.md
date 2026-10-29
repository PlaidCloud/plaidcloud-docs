---
title: GET_JSON_INT (Lakehouse v2)
description: GET_JSON_INT — extrae un valor entero de un objeto JSON mediante una ruta específica.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/get-json-int.md
---

Extrae un valor entero de un objeto JSON mediante una ruta específica.

## Sintaxis de Analyze

```python
func.get_json_int(get_column(table, 'data'), '$.age')
```

## Ejemplos de Analyze

```python
func.get_json_int(get_column(table, 'data'), '$.age')

┌────┐
│ 30 │
└────┘
```

## Sintaxis de SQL

```sql
GET_JSON_INT(<data>, '$.age')
```

## Ejemplos de SQL

```sql
SELECT GET_JSON_INT('{"age": 30}', '$.age');

┌────┐
│ 30 │
└────┘
```
