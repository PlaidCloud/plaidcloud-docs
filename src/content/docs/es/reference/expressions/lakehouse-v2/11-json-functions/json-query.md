---
title: JSON_QUERY (Lakehouse v2)
description: JSON_QUERY — extrae un valor JSON de un documento JSON mediante una expresión de ruta.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-query.md
---

Extrae un valor JSON de un documento JSON mediante una expresión de ruta.

## Sintaxis de Analyze

```python
func.json_query(get_column(table, 'data'), '$.items')
```

## Ejemplos de Analyze

```python
func.json_query(get_column(table, 'data'), '$.items')

┌────────────┐
│ JSON value │
└────────────┘
```

## Sintaxis de SQL

```sql
JSON_QUERY(<data>, '$.items')
```

## Ejemplos de SQL

```sql
SELECT JSON_QUERY(PARSE_JSON('{"items":[1,2,3]}'), '$.items');

┌─────────┐
│ [1,2,3] │
└─────────┘
```
