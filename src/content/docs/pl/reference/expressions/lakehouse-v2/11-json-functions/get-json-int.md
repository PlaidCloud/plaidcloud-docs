---
title: GET_JSON_INT (Lakehouse v2)
description: GET_JSON_INT — wyodrębnia wartość całkowitą z obiektu JSON na podstawie podanej ścieżki.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/get-json-int.md
---

Wyodrębnia wartość całkowitą z obiektu JSON na podstawie podanej ścieżki.

## Składnia Analyze

```python
func.get_json_int(get_column(table, 'data'), '$.age')
```

## Przykłady Analyze

```python
func.get_json_int(get_column(table, 'data'), '$.age')

┌────┐
│ 30 │
└────┘
```

## Składnia SQL

```sql
GET_JSON_INT(<data>, '$.age')
```

## Przykłady SQL

```sql
SELECT GET_JSON_INT('{"age": 30}', '$.age');

┌────┐
│ 30 │
└────┘
```
