---
title: NEGATIVE (Lakehouse v2)
description: NEGATIVE — zwraca liczbę przeciwną do podanej.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/negative.md
---

Zwraca liczbę przeciwną do podanej.

## Składnia Analyze

```python
func.negative(<x>)
```

## Przykłady Analyze

```python
func.negative(5)

┌────┐
│ -5  │
└────┘
```

## Składnia SQL

```sql
NEGATIVE(<x>)
```

## Przykłady SQL

```sql
SELECT NEGATIVE(5);

┌────┐
│ -5  │
└────┘
```
