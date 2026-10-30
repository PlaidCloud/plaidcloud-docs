---
title: GET_JSON_OBJECT (Lakehouse v2)
description: GET_JSON_OBJECT — extrait un objet JSON d'une chaîne JSON à partir d'un chemin spécifié.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/get-json-object.md
---

Extrait un objet JSON d'une chaîne JSON à partir d'un chemin spécifié.

## Syntaxe Analyze

```python
func.get_json_object(get_column(table, 'data'), '$.address')
```

## Exemples Analyze

```python
func.get_json_object(get_column(table, 'data'), '$.address')

┌─────────────┐
│ JSON object │
└─────────────┘
```

## Syntaxe SQL

```sql
GET_JSON_OBJECT(<data>, '$.address')
```

## Exemples SQL

```sql
SELECT GET_JSON_OBJECT('{"address":{"city":"NYC"}}', '$.address');

┌────────────────┐
│ {"city":"NYC"} │
└────────────────┘
```
