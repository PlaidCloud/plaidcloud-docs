---
title: JSON_REMOVE (Lakehouse v2)
description: JSON_REMOVE – entfernt ein Element an einem angegebenen Pfad aus einem JSON-Dokument.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-remove.md
---

Entfernt ein Element an einem angegebenen Pfad aus einem JSON-Dokument.

## Analyze-Syntax

```python
func.json_remove(get_column(table, 'data'), '$.temp')
```

## Analyze-Beispiele

```python
func.json_remove(get_column(table, 'data'), '$.temp')

┌──────────────────────┐
│ JSON without element │
└──────────────────────┘
```

## SQL-Syntax

```sql
JSON_REMOVE(<data>, '$.temp')
```

## SQL-Beispiele

```sql
SELECT JSON_REMOVE(PARSE_JSON('{"name":"Alice","temp":1}'), '$.temp');

┌──────────────────┐
│ {"name":"Alice"} │
└──────────────────┘
```
