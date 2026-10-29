---
title: JSON_SET (Lakehouse v2)
description: JSON_SET — définit une valeur dans un document JSON au chemin spécifié.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-set.md
---

Définit une valeur dans un document JSON au chemin spécifié.

## Syntaxe Analyze

```python
func.json_set(get_column(table, 'data'), '$.age', 31)
```

## Exemples Analyze

```python
func.json_set(get_column(table, 'data'), '$.age', 31)

┌──────────────┐
│ updated JSON │
└──────────────┘
```

## Syntaxe SQL

```sql
JSON_SET(<data>, '$.age', 31)
```

## Exemples SQL

```sql
SELECT JSON_SET(PARSE_JSON('{"name":"Alice"}'), '$.age', 30);

┌───────────────────────────┐
│ {"name":"Alice","age":30} │
└───────────────────────────┘
```
