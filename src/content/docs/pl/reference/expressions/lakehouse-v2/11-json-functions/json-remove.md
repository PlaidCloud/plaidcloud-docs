---
title: JSON_REMOVE (Lakehouse v2)
description: JSON_REMOVE — usuwa element z dokumentu JSON pod podaną ścieżką.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-remove.md
---

Usuwa element z dokumentu JSON pod podaną ścieżką.

## Składnia Analyze

```python
func.json_remove(get_column(table, 'data'), '$.temp')
```

## Przykłady Analyze

```python
func.json_remove(get_column(table, 'data'), '$.temp')

┌──────────────────────┐
│ JSON without element │
└──────────────────────┘
```

## Składnia SQL

```sql
JSON_REMOVE(<data>, '$.temp')
```

## Przykłady SQL

```sql
SELECT JSON_REMOVE(PARSE_JSON('{"name":"Alice","temp":1}'), '$.temp');

┌──────────────────┐
│ {"name":"Alice"} │
└──────────────────┘
```
