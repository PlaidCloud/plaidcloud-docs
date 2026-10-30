---
title: GET_JSON_OBJECT (Lakehouse v2)
description: GET_JSON_OBJECT — wyodrębnia obiekt JSON z ciągu znaków JSON na podstawie podanej ścieżki.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/get-json-object.md
---

Wyodrębnia obiekt JSON z ciągu znaków JSON na podstawie podanej ścieżki.

## Składnia Analyze

```python
func.get_json_object(get_column(table, 'data'), '$.address')
```

## Przykłady Analyze

```python
func.get_json_object(get_column(table, 'data'), '$.address')

┌─────────────┐
│ JSON object │
└─────────────┘
```

## Składnia SQL

```sql
GET_JSON_OBJECT(<data>, '$.address')
```

## Przykłady SQL

```sql
SELECT GET_JSON_OBJECT('{"address":{"city":"NYC"}}', '$.address');

┌────────────────┐
│ {"city":"NYC"} │
└────────────────┘
```
