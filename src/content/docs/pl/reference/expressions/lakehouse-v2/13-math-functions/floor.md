---
title: FLOOR (Lakehouse v2)
description: FLOOR — zwraca największą liczbę całkowitą mniejszą lub równą podanej liczbie.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/floor.md
---

Zwraca największą liczbę całkowitą mniejszą lub równą podanej liczbie.

## Składnia Analyze

```python
func.floor(<x>)
```

## Przykłady Analyze

```python
func.floor(3.7)

┌───┐
│ 3  │
└───┘
```

## Składnia SQL

```sql
FLOOR(<x>)
```

## Przykłady SQL

```sql
SELECT FLOOR(3.7);

┌───┐
│ 3  │
└───┘
```
