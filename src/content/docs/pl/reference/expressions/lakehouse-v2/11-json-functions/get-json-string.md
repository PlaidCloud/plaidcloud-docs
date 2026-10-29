---
title: GET_JSON_STRING (Lakehouse v2)
description: GET_JSON_STRING — wyodrębnia wartość tekstową z obiektu JSON na podstawie podanej ścieżki.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/get-json-string.md
---

Wyodrębnia wartość tekstową z obiektu JSON na podstawie podanej ścieżki.

## Składnia Analyze

```python
func.get_json_string(get_column(table, 'data'), '$.name')
```

## Przykłady Analyze

```python
func.get_json_string(get_column(table, 'data'), '$.name')

┌───────┐
│ Alice │
└───────┘
```

## Składnia SQL

```sql
GET_JSON_STRING(<data>, '$.name')
```

## Przykłady SQL

```sql
SELECT GET_JSON_STRING('{"name": "Alice"}', '$.name');

┌───────┐
│ Alice │
└───────┘
```
