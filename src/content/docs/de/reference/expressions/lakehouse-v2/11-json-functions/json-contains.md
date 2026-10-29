---
title: JSON_CONTAINS (Lakehouse v2)
description: JSON_CONTAINS – prüft, ob ein JSON-Dokument an einem Pfad einen bestimmten Wert enthält.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-contains.md
---

Prüft, ob ein JSON-Dokument an einem Pfad einen bestimmten Wert enthält.

## Analyze-Syntax

```python
func.json_contains(get_column(table, 'data'), '"Alice"', '$.name')
```

## Analyze-Beispiele

```python
func.json_contains(get_column(table, 'data'), '"Alice"', '$.name')

┌───┐
│ 1 │
└───┘
```

## SQL-Syntax

```sql
JSON_CONTAINS(<data>, '"Alice"', '$.name')
```

## SQL-Beispiele

```sql
SELECT JSON_CONTAINS('{"name":"Alice"}', '"Alice"', '$.name');

┌───┐
│ 1 │
└───┘
```
