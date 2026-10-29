---
title: JSON_REMOVE (Lakehouse v2)
description: JSON_REMOVE — elimina un elemento de un documento JSON en una ruta específica.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-remove.md
---

Elimina un elemento de un documento JSON en una ruta específica.

## Sintaxis de Analyze

```python
func.json_remove(get_column(table, 'data'), '$.temp')
```

## Ejemplos de Analyze

```python
func.json_remove(get_column(table, 'data'), '$.temp')

┌──────────────────────┐
│ JSON without element │
└──────────────────────┘
```

## Sintaxis de SQL

```sql
JSON_REMOVE(<data>, '$.temp')
```

## Ejemplos de SQL

```sql
SELECT JSON_REMOVE(PARSE_JSON('{"name":"Alice","temp":1}'), '$.temp');

┌──────────────────┐
│ {"name":"Alice"} │
└──────────────────┘
```
