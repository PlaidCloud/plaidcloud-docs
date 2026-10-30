---
title: CEILING (Lakehouse v2)
description: CEILING — zwraca najmniejszą liczbę całkowitą większą lub równą podanej liczbie. Alias funkcji `CEIL`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/ceiling.md
---

Zwraca najmniejszą liczbę całkowitą większą lub równą podanej liczbie. Alias funkcji `CEIL`.

## Składnia Analyze

```python
func.ceiling(<x>)
```

## Przykłady Analyze

```python
func.ceiling(3.2)

┌───┐
│ 4  │
└───┘
```

## Składnia SQL

```sql
CEILING(<x>)
```

## Przykłady SQL

```sql
SELECT CEILING(3.2);

┌───┐
│ 4  │
└───┘
```
