---
title: GET_JSON_BOOL (Lakehouse v2)
description: GET_JSON_BOOL – extrahiert einen booleschen Wert aus einem JSON-Objekt anhand eines angegebenen Pfads.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/get-json-bool.md
---

Extrahiert einen booleschen Wert aus einem JSON-Objekt anhand eines angegebenen Pfads.

## Analyze-Syntax

```python
func.get_json_bool(get_column(table, 'data'), '$.active')
```

## Analyze-Beispiele

```python
func.get_json_bool(get_column(table, 'data'), '$.active')

┌───┐
│ 1 │
└───┘
```

## SQL-Syntax

```sql
GET_JSON_BOOL(<data>, '$.active')
```

## SQL-Beispiele

```sql
SELECT GET_JSON_BOOL('{"active": true}', '$.active');

┌───┐
│ 1 │
└───┘
```
