---
title: JSON_EACH (Lakehouse v2)
description: JSON_EACH — développe l'objet JSON de premier niveau en un ensemble de paires clé-valeur.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-each.md
---

Développe l'objet JSON de premier niveau en un ensemble de paires clé-valeur.

## Syntaxe Analyze

```python
func.json_each(get_column(table, 'data'))
```

## Exemples Analyze

```python
func.json_each(get_column(table, 'data'))
```

## Syntaxe SQL

```sql
JSON_EACH(<data>)
```

## Exemples SQL

```sql
SELECT * FROM TABLE(JSON_EACH(PARSE_JSON('{"a":1,"b":2}')));

┌─────┬───────┐
│ key │ value │
├─────┼───────┤
│ a   │ 1     │
│ b   │ 2     │
└─────┴───────┘
```
