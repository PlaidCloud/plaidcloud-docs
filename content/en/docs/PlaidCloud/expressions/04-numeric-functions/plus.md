---
title: PLUS
---

Calculates the sum of two numeric or decimal values.

## Analyze Syntax

```python
func.plus(<number1>, <number2>)
```

## Analyze Examples

```python
func.plus(1, 2.3)

┌────────────────────┐
│  func.plus(1, 2.3) │
├────────────────────┤
│ 3.3                │
└────────────────────┘
```

## SQL Syntax

```sql
PLUS(<number1>, <number2>)
```

## Aliases

- [ADD](../add)

## SQL Examples

```sql
SELECT ADD(1, 2.3), PLUS(1, 2.3);

┌───────────────────────────────┐
│  add(1, 2.3)  │  plus(1, 2.3) │
├───────────────┼───────────────┤
│ 3.3           │ 3.3           │
└───────────────────────────────┘
```