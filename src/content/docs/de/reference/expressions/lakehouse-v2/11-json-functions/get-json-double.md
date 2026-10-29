---
title: GET_JSON_DOUBLE (Lakehouse v2)
description: GET_JSON_DOUBLE – extrahiert einen Double-Wert aus einem JSON-Objekt anhand eines angegebenen Pfads.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/get-json-double.md
---

Extrahiert einen Double-Wert aus einem JSON-Objekt anhand eines angegebenen Pfads.

## Analyze-Syntax

```python
func.get_json_double(get_column(table, 'data'), '$.price')
```

## Analyze-Beispiele

```python
func.get_json_double(get_column(table, 'data'), '$.price')

┌───────┐
│ 19.99 │
└───────┘
```

## SQL-Syntax

```sql
GET_JSON_DOUBLE(<data>, '$.price')
```

## SQL-Beispiele

```sql
SELECT GET_JSON_DOUBLE('{"price": 19.99}', '$.price');

┌───────┐
│ 19.99 │
└───────┘
```
