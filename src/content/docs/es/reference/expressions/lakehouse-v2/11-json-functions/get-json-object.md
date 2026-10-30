---
title: GET_JSON_OBJECT (Lakehouse v2)
description: GET_JSON_OBJECT — extrae un objeto JSON de una cadena JSON mediante una ruta específica.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/get-json-object.md
---

Extrae un objeto JSON de una cadena JSON mediante una ruta específica.

## Sintaxis de Analyze

```python
func.get_json_object(get_column(table, 'data'), '$.address')
```

## Ejemplos de Analyze

```python
func.get_json_object(get_column(table, 'data'), '$.address')

┌─────────────┐
│ JSON object │
└─────────────┘
```

## Sintaxis de SQL

```sql
GET_JSON_OBJECT(<data>, '$.address')
```

## Ejemplos de SQL

```sql
SELECT GET_JSON_OBJECT('{"address":{"city":"NYC"}}', '$.address');

┌────────────────┐
│ {"city":"NYC"} │
└────────────────┘
```
