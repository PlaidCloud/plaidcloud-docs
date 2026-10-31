---
title: JSON_LENGTH (Lakehouse v2)
description: JSON_LENGTH — renvoie le nombre d'éléments d'un objet ou tableau JSON.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-length.md
---

Renvoie le nombre d'éléments d'un objet ou tableau JSON.

## Syntaxe Analyze

```python
func.json_length(get_column(table, 'data'))
```

## Exemples Analyze

```python
func.json_length(get_column(table, 'data'))

┌───┐
│ 2 │
└───┘
```

## Syntaxe SQL

```sql
JSON_LENGTH(<data>)
```

## Exemples SQL

```sql
SELECT JSON_LENGTH(PARSE_JSON('{"name":"Alice","age":30}'));

┌───┐
│ 2 │
└───┘
```
