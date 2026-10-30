---
title: JSON_KEYS (Lakehouse v2)
description: JSON_KEYS — renvoie les clés de l'objet JSON de premier niveau sous forme de tableau JSON.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-keys.md
---

Renvoie les clés de l'objet JSON de premier niveau sous forme de tableau JSON.

## Syntaxe Analyze

```python
func.json_keys(get_column(table, 'data'))
```

## Exemples Analyze

```python
func.json_keys(get_column(table, 'data'))

┌────────────────┐
│ ["name","age"] │
└────────────────┘
```

## Syntaxe SQL

```sql
JSON_KEYS(<data>)
```

## Exemples SQL

```sql
SELECT JSON_KEYS(PARSE_JSON('{"name":"Alice","age":30}'));

┌────────────────┐
│ ["name","age"] │
└────────────────┘
```
