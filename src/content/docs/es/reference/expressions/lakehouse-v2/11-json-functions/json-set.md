---
title: JSON_SET (Lakehouse v2)
description: JSON_SET — establece un valor en un documento JSON en una ruta específica.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-set.md
---

Establece un valor en un documento JSON en una ruta específica.

## Sintaxis de Analyze

```python
func.json_set(get_column(table, 'data'), '$.age', 31)
```

## Ejemplos de Analyze

```python
func.json_set(get_column(table, 'data'), '$.age', 31)

┌──────────────┐
│ updated JSON │
└──────────────┘
```

## Sintaxis de SQL

```sql
JSON_SET(<data>, '$.age', 31)
```

## Ejemplos de SQL

```sql
SELECT JSON_SET(PARSE_JSON('{"name":"Alice"}'), '$.age', 30);

┌───────────────────────────┐
│ {"name":"Alice","age":30} │
└───────────────────────────┘
```
