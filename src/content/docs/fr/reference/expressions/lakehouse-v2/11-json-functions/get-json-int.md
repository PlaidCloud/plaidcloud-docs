---
title: GET_JSON_INT (Lakehouse v2)
description: GET_JSON_INT — extrait une valeur entière d'un objet JSON à partir d'un chemin spécifié.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/get-json-int.md
---

Extrait une valeur entière d'un objet JSON à partir d'un chemin spécifié.

## Syntaxe Analyze

```python
func.get_json_int(get_column(table, 'data'), '$.age')
```

## Exemples Analyze

```python
func.get_json_int(get_column(table, 'data'), '$.age')

┌────┐
│ 30 │
└────┘
```

## Syntaxe SQL

```sql
GET_JSON_INT(<data>, '$.age')
```

## Exemples SQL

```sql
SELECT GET_JSON_INT('{"age": 30}', '$.age');

┌────┐
│ 30 │
└────┘
```
