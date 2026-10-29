---
title: JSON_SET (Lakehouse v2)
description: JSON_SET — ustawia wartość w dokumencie JSON pod podaną ścieżką.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-set.md
---

Ustawia wartość w dokumencie JSON pod podaną ścieżką.

## Składnia Analyze

```python
func.json_set(get_column(table, 'data'), '$.age', 31)
```

## Przykłady Analyze

```python
func.json_set(get_column(table, 'data'), '$.age', 31)

┌──────────────┐
│ updated JSON │
└──────────────┘
```

## Składnia SQL

```sql
JSON_SET(<data>, '$.age', 31)
```

## Przykłady SQL

```sql
SELECT JSON_SET(PARSE_JSON('{"name":"Alice"}'), '$.age', 30);

┌───────────────────────────┐
│ {"name":"Alice","age":30} │
└───────────────────────────┘
```
