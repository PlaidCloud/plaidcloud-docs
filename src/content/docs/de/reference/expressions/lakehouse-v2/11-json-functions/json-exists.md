---
title: JSON_EXISTS (Lakehouse v2)
description: JSON_EXISTS – prüft, ob ein JSON-Dokument an einem angegebenen Pfad einen Wert enthält.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-exists.md
---

Prüft, ob ein JSON-Dokument an einem angegebenen Pfad einen Wert enthält.

## Analyze-Syntax

```python
func.json_exists(get_column(table, 'data'), '$.name')
```

## Analyze-Beispiele

```python
func.json_exists(get_column(table, 'data'), '$.name')

┌───┐
│ 1 │
└───┘
```

## SQL-Syntax

```sql
JSON_EXISTS(<data>, '$.name')
```

## SQL-Beispiele

```sql
SELECT JSON_EXISTS(PARSE_JSON('{"name":"Alice"}'), '$.name');

┌───┐
│ 1 │
└───┘
```
