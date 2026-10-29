---
title: JSON_QUERY (Lakehouse v2)
description: JSON_QUERY – extrahiert mithilfe eines Pfadausdrucks einen JSON-Wert aus einem JSON-Dokument.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-query.md
---

Extrahiert mithilfe eines Pfadausdrucks einen JSON-Wert aus einem JSON-Dokument.

## Analyze-Syntax

```python
func.json_query(get_column(table, 'data'), '$.items')
```

## Analyze-Beispiele

```python
func.json_query(get_column(table, 'data'), '$.items')

┌────────────┐
│ JSON value │
└────────────┘
```

## SQL-Syntax

```sql
JSON_QUERY(<data>, '$.items')
```

## SQL-Beispiele

```sql
SELECT JSON_QUERY(PARSE_JSON('{"items":[1,2,3]}'), '$.items');

┌─────────┐
│ [1,2,3] │
└─────────┘
```
