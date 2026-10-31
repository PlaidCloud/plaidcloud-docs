---
title: GET_JSON_BOOL (Lakehouse v2)
description: GET_JSON_BOOL — wyodrębnia wartość logiczną z obiektu JSON na podstawie podanej ścieżki.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/get-json-bool.md
---

Wyodrębnia wartość logiczną z obiektu JSON na podstawie podanej ścieżki.

## Składnia Analyze

```python
func.get_json_bool(get_column(table, 'data'), '$.active')
```

## Przykłady Analyze

```python
func.get_json_bool(get_column(table, 'data'), '$.active')

┌───┐
│ 1 │
└───┘
```

## Składnia SQL

```sql
GET_JSON_BOOL(<data>, '$.active')
```

## Przykłady SQL

```sql
SELECT GET_JSON_BOOL('{"active": true}', '$.active');

┌───┐
│ 1 │
└───┘
```
