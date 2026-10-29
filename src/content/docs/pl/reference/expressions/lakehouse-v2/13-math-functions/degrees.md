---
title: DEGREES (Lakehouse v2)
description: DEGREES — konwertuje radiany na stopnie.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/degrees.md
---

Konwertuje radiany na stopnie.

## Składnia Analyze

```python
func.degrees(<x>)
```

## Przykłady Analyze

```python
func.degrees(3.141592653589793)

┌───────┐
│ 180.0  │
└───────┘
```

## Składnia SQL

```sql
DEGREES(<x>)
```

## Przykłady SQL

```sql
SELECT DEGREES(PI());

┌───────┐
│ 180.0  │
└───────┘
```
