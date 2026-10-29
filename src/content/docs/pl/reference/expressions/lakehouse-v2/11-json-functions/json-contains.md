---
title: JSON_CONTAINS (Lakehouse v2)
description: JSON_CONTAINS — sprawdza, czy dokument JSON zawiera określoną wartość pod wskazaną ścieżką.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-contains.md
---

Sprawdza, czy dokument JSON zawiera określoną wartość pod wskazaną ścieżką.

## Składnia Analyze

```python
func.json_contains(get_column(table, 'data'), '"Alice"', '$.name')
```

## Przykłady Analyze

```python
func.json_contains(get_column(table, 'data'), '"Alice"', '$.name')

┌───┐
│ 1 │
└───┘
```

## Składnia SQL

```sql
JSON_CONTAINS(<data>, '"Alice"', '$.name')
```

## Przykłady SQL

```sql
SELECT JSON_CONTAINS('{"name":"Alice"}', '"Alice"', '$.name');

┌───┐
│ 1 │
└───┘
```
