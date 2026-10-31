---
title: JSON_LENGTH (Lakehouse v2)
description: JSON_LENGTH — devuelve el número de elementos de un objeto o matriz JSON.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-length.md
---

Devuelve el número de elementos de un objeto o matriz JSON.

## Sintaxis de Analyze

```python
func.json_length(get_column(table, 'data'))
```

## Ejemplos de Analyze

```python
func.json_length(get_column(table, 'data'))

┌───┐
│ 2 │
└───┘
```

## Sintaxis de SQL

```sql
JSON_LENGTH(<data>)
```

## Ejemplos de SQL

```sql
SELECT JSON_LENGTH(PARSE_JSON('{"name":"Alice","age":30}'));

┌───┐
│ 2 │
└───┘
```
