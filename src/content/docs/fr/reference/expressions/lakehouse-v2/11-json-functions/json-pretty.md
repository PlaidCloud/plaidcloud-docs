---
title: JSON_PRETTY (Lakehouse v2)
description: JSON_PRETTY — met en forme une valeur JSON avec indentation pour en faciliter la lecture.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-pretty.md
---

Met en forme une valeur JSON avec indentation pour en faciliter la lecture.

## Syntaxe Analyze

```python
func.json_pretty(get_column(table, 'data'))
```

## Exemples Analyze

```python
func.json_pretty(get_column(table, 'data'))

┌──────────────────┐
│ (formatted JSON) │
└──────────────────┘
```

## Syntaxe SQL

```sql
JSON_PRETTY(<data>)
```

## Exemples SQL

```sql
SELECT JSON_PRETTY(PARSE_JSON('{"name":"Alice","age":30}'));

┌────────────────────────────────────┐
│ {
  "name": "Alice",
  "age": 30
} │
└────────────────────────────────────┘
```
