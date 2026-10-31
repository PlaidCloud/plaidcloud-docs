---
title: GET_JSON_STRING (Lakehouse v2)
description: GET_JSON_STRING — extrait une valeur de type chaîne d'un objet JSON à partir d'un chemin spécifié.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/get-json-string.md
---

Extrait une valeur de type chaîne d'un objet JSON à partir d'un chemin spécifié.

## Syntaxe Analyze

```python
func.get_json_string(get_column(table, 'data'), '$.name')
```

## Exemples Analyze

```python
func.get_json_string(get_column(table, 'data'), '$.name')

┌───────┐
│ Alice │
└───────┘
```

## Syntaxe SQL

```sql
GET_JSON_STRING(<data>, '$.name')
```

## Exemples SQL

```sql
SELECT GET_JSON_STRING('{"name": "Alice"}', '$.name');

┌───────┐
│ Alice │
└───────┘
```
