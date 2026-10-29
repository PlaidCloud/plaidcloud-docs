---
title: DIV0 (Lakehouse v1)
description: DIV0 – gibt den Quotienten aus der Division der ersten Zahl durch die zweite zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/div0.md
---

Gibt den Quotienten aus der Division der ersten Zahl durch die zweite zurück. Gibt 0 zurück, wenn die zweite Zahl 0 ist.

Siehe auch:

- [DIV](../div)
- [DIVNULL](../divnull)

## Analyze-Syntax

```python
func.div0(<numerator>, <denominator>)
```

## Analyze-Beispiele

```python
func.div0(20, 6), func.div0(20, 0), func.div0(20, null)

┌─────────────────────────────────────────────────────────────┐
│  func.div0(20, 6)  │ func.div0(20, 0) │ func.div0(20, null) │
├────────────────────┼──────────────────┼─────────────────────┤
│ 3.3333333333333335 │                0 │ NULL                │
└─────────────────────────────────────────────────────────────┘
```

## SQL-Syntax

```sql
DIV0(<number1>, <number2>)
```

## SQL-Beispiele

```sql
SELECT
  DIV0(20, 6),
  DIV0(20, 0),
  DIV0(20, NULL);

┌───────────────────────────────────────────────────┐
│     div0(20, 6)    │ div0(20, 0) │ div0(20, null) │
├────────────────────┼─────────────┼────────────────┤
│ 3.3333333333333335 │           0 │ NULL           │
└───────────────────────────────────────────────────┘
```
