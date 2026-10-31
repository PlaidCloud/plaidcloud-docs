---
title: JSON_CONTAINS (Lakehouse v2)
description: JSON_CONTAINS — comprueba si un documento JSON contiene un valor específico en una ruta.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-contains.md
---

Comprueba si un documento JSON contiene un valor específico en una ruta.

## Sintaxis de Analyze

```python
func.json_contains(get_column(table, 'data'), '"Alice"', '$.name')
```

## Ejemplos de Analyze

```python
func.json_contains(get_column(table, 'data'), '"Alice"', '$.name')

┌───┐
│ 1 │
└───┘
```

## Sintaxis de SQL

```sql
JSON_CONTAINS(<data>, '"Alice"', '$.name')
```

## Ejemplos de SQL

```sql
SELECT JSON_CONTAINS('{"name":"Alice"}', '"Alice"', '$.name');

┌───┐
│ 1 │
└───┘
```
