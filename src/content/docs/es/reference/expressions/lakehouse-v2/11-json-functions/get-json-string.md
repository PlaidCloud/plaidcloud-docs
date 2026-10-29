---
title: GET_JSON_STRING (Lakehouse v2)
description: GET_JSON_STRING — extrae un valor de cadena de un objeto JSON mediante una ruta específica.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/get-json-string.md
---

Extrae un valor de cadena de un objeto JSON mediante una ruta específica.

## Sintaxis de Analyze

```python
func.get_json_string(get_column(table, 'data'), '$.name')
```

## Ejemplos de Analyze

```python
func.get_json_string(get_column(table, 'data'), '$.name')

┌───────┐
│ Alice │
└───────┘
```

## Sintaxis de SQL

```sql
GET_JSON_STRING(<data>, '$.name')
```

## Ejemplos de SQL

```sql
SELECT GET_JSON_STRING('{"name": "Alice"}', '$.name');

┌───────┐
│ Alice │
└───────┘
```
