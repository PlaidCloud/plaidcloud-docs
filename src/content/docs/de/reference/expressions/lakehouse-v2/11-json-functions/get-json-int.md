---
title: GET_JSON_INT (Lakehouse v2)
description: GET_JSON_INT – extrahiert einen Ganzzahlwert aus einem JSON-Objekt anhand eines angegebenen Pfads.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/get-json-int.md
---

Extrahiert einen Ganzzahlwert aus einem JSON-Objekt anhand eines angegebenen Pfads.

## Analyze-Syntax

```python
func.get_json_int(get_column(table, 'data'), '$.age')
```

## Analyze-Beispiele

```python
func.get_json_int(get_column(table, 'data'), '$.age')

┌────┐
│ 30 │
└────┘
```

## SQL-Syntax

```sql
GET_JSON_INT(<data>, '$.age')
```

## SQL-Beispiele

```sql
SELECT GET_JSON_INT('{"age": 30}', '$.age');

┌────┐
│ 30 │
└────┘
```
