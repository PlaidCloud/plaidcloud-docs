---
title: ABS (Lakehouse v2)
description: ABS — zwraca wartość bezwzględną liczby.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/abs.md
---

Zwraca wartość bezwzględną liczby.

## Składnia Analyze

```python
func.abs(<x>)
```

## Przykłady Analyze

```python
func.abs(-5)

┌───┐
│ 5  │
└───┘
```

## Składnia SQL

```sql
ABS(<x>)
```

## Przykłady SQL

```sql
SELECT ABS(-5);

┌───┐
│ 5  │
└───┘
```
