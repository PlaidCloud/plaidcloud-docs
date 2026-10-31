---
title: JSON_LENGTH (Lakehouse v2)
description: JSON_LENGTH — zwraca liczbę elementów w obiekcie lub tablicy JSON.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-length.md
---

Zwraca liczbę elementów w obiekcie lub tablicy JSON.

## Składnia Analyze

```python
func.json_length(get_column(table, 'data'))
```

## Przykłady Analyze

```python
func.json_length(get_column(table, 'data'))

┌───┐
│ 2 │
└───┘
```

## Składnia SQL

```sql
JSON_LENGTH(<data>)
```

## Przykłady SQL

```sql
SELECT JSON_LENGTH(PARSE_JSON('{"name":"Alice","age":30}'));

┌───┐
│ 2 │
└───┘
```
