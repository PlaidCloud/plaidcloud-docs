---
title: GET_JSON_STRING (Lakehouse v2)
description: GET_JSON_STRING – extrahiert einen Zeichenfolgenwert aus einem JSON-Objekt anhand eines angegebenen Pfads.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/get-json-string.md
---

Extrahiert einen Zeichenfolgenwert aus einem JSON-Objekt anhand eines angegebenen Pfads.

## Analyze-Syntax

```python
func.get_json_string(get_column(table, 'data'), '$.name')
```

## Analyze-Beispiele

```python
func.get_json_string(get_column(table, 'data'), '$.name')

┌───────┐
│ Alice │
└───────┘
```

## SQL-Syntax

```sql
GET_JSON_STRING(<data>, '$.name')
```

## SQL-Beispiele

```sql
SELECT GET_JSON_STRING('{"name": "Alice"}', '$.name');

┌───────┐
│ Alice │
└───────┘
```
