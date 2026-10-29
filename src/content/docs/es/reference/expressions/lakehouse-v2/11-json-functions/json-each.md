---
title: JSON_EACH (Lakehouse v2)
description: JSON_EACH — expande el objeto JSON de nivel superior en un conjunto de pares clave-valor.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-each.md
---

Expande el objeto JSON de nivel superior en un conjunto de pares clave-valor.

## Sintaxis de Analyze

```python
func.json_each(get_column(table, 'data'))
```

## Ejemplos de Analyze

```python
func.json_each(get_column(table, 'data'))
```

## Sintaxis de SQL

```sql
JSON_EACH(<data>)
```

## Ejemplos de SQL

```sql
SELECT * FROM TABLE(JSON_EACH(PARSE_JSON('{"a":1,"b":2}')));

┌─────┬───────┐
│ key │ value │
├─────┼───────┤
│ a   │ 1     │
│ b   │ 2     │
└─────┴───────┘
```
