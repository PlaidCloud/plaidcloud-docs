---
title: ALL_MATCH (Lakehouse v2)
description: ALL_MATCH – gibt TRUE zurück, wenn alle Elemente eines Arrays dem angegebenen Prädikat entsprechen.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/all-match.md
---

Gibt TRUE zurück, wenn alle Elemente eines Arrays dem angegebenen Prädikat entsprechen.

## Analyze-Syntax

```python
func.all_match(get_column(table, 'arr'), lambda x: x > 0)
```

## Analyze-Beispiele

```python
func.all_match([1, 2, 3], lambda x: x > 0)

┌───┐
│ 1 │
└───┘
```

## SQL-Syntax

```sql
ALL_MATCH(<arr>, lambda x: x > 0)
```

## SQL-Beispiele

```sql
SELECT ALL_MATCH([1, 2, 3], x -> x > 0);

┌───┐
│ 1 │
└───┘
```
