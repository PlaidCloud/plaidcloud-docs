---
title: GET_JSON_BOOL (Lakehouse v2)
description: GET_JSON_BOOL — extrait une valeur booléenne d'un objet JSON à partir d'un chemin spécifié.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/get-json-bool.md
---

Extrait une valeur booléenne d'un objet JSON à partir d'un chemin spécifié.

## Syntaxe Analyze

```python
func.get_json_bool(get_column(table, 'data'), '$.active')
```

## Exemples Analyze

```python
func.get_json_bool(get_column(table, 'data'), '$.active')

┌───┐
│ 1 │
└───┘
```

## Syntaxe SQL

```sql
GET_JSON_BOOL(<data>, '$.active')
```

## Exemples SQL

```sql
SELECT GET_JSON_BOOL('{"active": true}', '$.active');

┌───┐
│ 1 │
└───┘
```
