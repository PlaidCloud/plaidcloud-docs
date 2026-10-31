---
title: JSON_LENGTH (Lakehouse v2)
description: JSON_LENGTH – gibt die Anzahl der Elemente in einem JSON-Objekt oder -Array zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-length.md
---

Gibt die Anzahl der Elemente in einem JSON-Objekt oder -Array zurück.

## Analyze-Syntax

```python
func.json_length(get_column(table, 'data'))
```

## Analyze-Beispiele

```python
func.json_length(get_column(table, 'data'))

┌───┐
│ 2 │
└───┘
```

## SQL-Syntax

```sql
JSON_LENGTH(<data>)
```

## SQL-Beispiele

```sql
SELECT JSON_LENGTH(PARSE_JSON('{"name":"Alice","age":30}'));

┌───┐
│ 2 │
└───┘
```
