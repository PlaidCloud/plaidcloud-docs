---
title: DIVNULL (Lakehouse v1)
description: DIVNULL – gibt den Quotienten aus der Division der ersten Zahl durch die zweite zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/divnull.md
---

Gibt den Quotienten aus der Division der ersten Zahl durch die zweite zurück. Gibt NULL zurück, wenn die zweite Zahl 0 oder NULL ist.

Siehe auch:

- [DIV](../div)
- [DIV0](../div0)

## Analyze-Syntax

```python
func.divnull(<numerator>, <denominator>)
```

## Analyze-Beispiele

```python
func.divnull(20, 6), func.divnull(20, 0), func.divnull(20, null)

┌───────────────────────────────────────────────────────────────────┐
│ func.divnull(20, 6)│ func.divnull(20, 0) │ func.divnull(20, null) │
├────────────────────┼─────────────────────┼────────────────────────┤
│ 3.3333333333333335 │ NULL                │ NULL                   │
└───────────────────────────────────────────────────────────────────┘
```

## SQL-Syntax

```sql
DIVNULL(<number1>, <number2>)
```

## SQL-Beispiele

```sql
SELECT
  DIVNULL(20, 6),
  DIVNULL(20, 0),
  DIVNULL(20, NULL);

┌─────────────────────────────────────────────────────────┐
│   divnull(20, 6)   │ divnull(20, 0) │ divnull(20, null) │
├────────────────────┼────────────────┼───────────────────┤
│ 3.3333333333333335 │ NULL           │ NULL              │
└─────────────────────────────────────────────────────────┘
```
