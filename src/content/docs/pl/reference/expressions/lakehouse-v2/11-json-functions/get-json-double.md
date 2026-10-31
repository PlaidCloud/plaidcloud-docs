---
title: GET_JSON_DOUBLE (Lakehouse v2)
description: GET_JSON_DOUBLE — wyodrębnia wartość typu double z obiektu JSON na podstawie podanej ścieżki.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/get-json-double.md
---

Wyodrębnia wartość typu double z obiektu JSON na podstawie podanej ścieżki.

## Składnia Analyze

```python
func.get_json_double(get_column(table, 'data'), '$.price')
```

## Przykłady Analyze

```python
func.get_json_double(get_column(table, 'data'), '$.price')

┌───────┐
│ 19.99 │
└───────┘
```

## Składnia SQL

```sql
GET_JSON_DOUBLE(<data>, '$.price')
```

## Przykłady SQL

```sql
SELECT GET_JSON_DOUBLE('{"price": 19.99}', '$.price');

┌───────┐
│ 19.99 │
└───────┘
```
