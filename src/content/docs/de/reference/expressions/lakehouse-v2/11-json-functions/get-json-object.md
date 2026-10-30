---
title: GET_JSON_OBJECT (Lakehouse v2)
description: GET_JSON_OBJECT – extrahiert ein JSON-Objekt aus einer JSON-Zeichenfolge anhand eines angegebenen Pfads.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/get-json-object.md
---

Extrahiert ein JSON-Objekt aus einer JSON-Zeichenfolge anhand eines angegebenen Pfads.

## Analyze-Syntax

```python
func.get_json_object(get_column(table, 'data'), '$.address')
```

## Analyze-Beispiele

```python
func.get_json_object(get_column(table, 'data'), '$.address')

┌─────────────┐
│ JSON object │
└─────────────┘
```

## SQL-Syntax

```sql
GET_JSON_OBJECT(<data>, '$.address')
```

## SQL-Beispiele

```sql
SELECT GET_JSON_OBJECT('{"address":{"city":"NYC"}}', '$.address');

┌────────────────┐
│ {"city":"NYC"} │
└────────────────┘
```
