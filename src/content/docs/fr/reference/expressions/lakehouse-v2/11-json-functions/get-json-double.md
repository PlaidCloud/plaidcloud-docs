---
title: GET_JSON_DOUBLE (Lakehouse v2)
description: GET_JSON_DOUBLE — extrait une valeur de type double d'un objet JSON à partir d'un chemin spécifié.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/get-json-double.md
---

Extrait une valeur de type double d'un objet JSON à partir d'un chemin spécifié.

## Syntaxe Analyze

```python
func.get_json_double(get_column(table, 'data'), '$.price')
```

## Exemples Analyze

```python
func.get_json_double(get_column(table, 'data'), '$.price')

┌───────┐
│ 19.99 │
└───────┘
```

## Syntaxe SQL

```sql
GET_JSON_DOUBLE(<data>, '$.price')
```

## Exemples SQL

```sql
SELECT GET_JSON_DOUBLE('{"price": 19.99}', '$.price');

┌───────┐
│ 19.99 │
└───────┘
```
