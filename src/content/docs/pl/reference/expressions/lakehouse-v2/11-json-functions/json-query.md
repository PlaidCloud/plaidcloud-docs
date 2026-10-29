---
title: JSON_QUERY (Lakehouse v2)
description: JSON_QUERY — wyodrębnia wartość JSON z dokumentu JSON za pomocą wyrażenia ścieżki.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-query.md
---

Wyodrębnia wartość JSON z dokumentu JSON za pomocą wyrażenia ścieżki.

## Składnia Analyze

```python
func.json_query(get_column(table, 'data'), '$.items')
```

## Przykłady Analyze

```python
func.json_query(get_column(table, 'data'), '$.items')

┌────────────┐
│ JSON value │
└────────────┘
```

## Składnia SQL

```sql
JSON_QUERY(<data>, '$.items')
```

## Przykłady SQL

```sql
SELECT JSON_QUERY(PARSE_JSON('{"items":[1,2,3]}'), '$.items');

┌─────────┐
│ [1,2,3] │
└─────────┘
```
