---
title: JSON_KEYS (Lakehouse v2)
description: JSON_KEYS — devuelve las claves del objeto JSON de nivel superior como una matriz JSON.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-keys.md
---

Devuelve las claves del objeto JSON de nivel superior como una matriz JSON.

## Sintaxis de Analyze

```python
func.json_keys(get_column(table, 'data'))
```

## Ejemplos de Analyze

```python
func.json_keys(get_column(table, 'data'))

┌────────────────┐
│ ["name","age"] │
└────────────────┘
```

## Sintaxis de SQL

```sql
JSON_KEYS(<data>)
```

## Ejemplos de SQL

```sql
SELECT JSON_KEYS(PARSE_JSON('{"name":"Alice","age":30}'));

┌────────────────┐
│ ["name","age"] │
└────────────────┘
```
