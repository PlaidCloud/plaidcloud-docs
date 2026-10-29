---
title: JSON_EXISTS (Lakehouse v2)
description: JSON_EXISTS — sprawdza, czy dokument JSON zawiera wartość pod podaną ścieżką.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-exists.md
---

Sprawdza, czy dokument JSON zawiera wartość pod podaną ścieżką.

## Składnia Analyze

```python
func.json_exists(get_column(table, 'data'), '$.name')
```

## Przykłady Analyze

```python
func.json_exists(get_column(table, 'data'), '$.name')

┌───┐
│ 1 │
└───┘
```

## Składnia SQL

```sql
JSON_EXISTS(<data>, '$.name')
```

## Przykłady SQL

```sql
SELECT JSON_EXISTS(PARSE_JSON('{"name":"Alice"}'), '$.name');

┌───┐
│ 1 │
└───┘
```
