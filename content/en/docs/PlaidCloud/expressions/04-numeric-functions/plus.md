---
title: PLUS
---

Calculates the sum of two numeric or decimal values.

## SQL Syntax

```sql
PLUS(<number1>, <number2>)
```

## Aliases

- [ADD](add)

## SQL Examples

```sql
SELECT ADD(1, 2.3), PLUS(1, 2.3);

┌───────────────────────────────┐
│  add(1, 2.3)  │  plus(1, 2.3) │
├───────────────┼───────────────┤
│ 3.3           │ 3.3           │
└───────────────────────────────┘
```