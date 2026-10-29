---
title: JSON_EXISTS (Lakehouse v2)
description: JSON_EXISTS — comprueba si un documento JSON contiene un valor en una ruta específica.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-exists.md
---

Comprueba si un documento JSON contiene un valor en una ruta específica.

## Sintaxis de Analyze

```python
func.json_exists(get_column(table, 'data'), '$.name')
```

## Ejemplos de Analyze

```python
func.json_exists(get_column(table, 'data'), '$.name')

┌───┐
│ 1 │
└───┘
```

## Sintaxis de SQL

```sql
JSON_EXISTS(<data>, '$.name')
```

## Ejemplos de SQL

```sql
SELECT JSON_EXISTS(PARSE_JSON('{"name":"Alice"}'), '$.name');

┌───┐
│ 1 │
└───┘
```
