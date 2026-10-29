---
title: JSON_SET (Lakehouse v2)
description: JSON_SET – setzt einen Wert an einem angegebenen Pfad in einem JSON-Dokument.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-set.md
---

Setzt einen Wert an einem angegebenen Pfad in einem JSON-Dokument.

## Analyze-Syntax

```python
func.json_set(get_column(table, 'data'), '$.age', 31)
```

## Analyze-Beispiele

```python
func.json_set(get_column(table, 'data'), '$.age', 31)

┌──────────────┐
│ updated JSON │
└──────────────┘
```

## SQL-Syntax

```sql
JSON_SET(<data>, '$.age', 31)
```

## SQL-Beispiele

```sql
SELECT JSON_SET(PARSE_JSON('{"name":"Alice"}'), '$.age', 30);

┌───────────────────────────┐
│ {"name":"Alice","age":30} │
└───────────────────────────┘
```
