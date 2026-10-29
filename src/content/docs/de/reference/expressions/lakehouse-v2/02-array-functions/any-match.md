---
title: ANY_MATCH (Lakehouse v2)
description: ANY_MATCH – gibt TRUE zurück, wenn mindestens ein Element eines Arrays dem angegebenen Prädikat entspricht.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/any-match.md
---

Gibt TRUE zurück, wenn mindestens ein Element eines Arrays dem angegebenen Prädikat entspricht.

## Analyze-Syntax

```python
func.any_match(get_column(table, 'arr'), lambda x: x > 5)
```

## Analyze-Beispiele

```python
func.any_match([1, 2, 8], lambda x: x > 5)

┌───┐
│ 1 │
└───┘
```

## SQL-Syntax

```sql
ANY_MATCH(<arr>, lambda x: x > 5)
```

## SQL-Beispiele

```sql
SELECT ANY_MATCH([1, 2, 8], x -> x > 5);

┌───┐
│ 1 │
└───┘
```
