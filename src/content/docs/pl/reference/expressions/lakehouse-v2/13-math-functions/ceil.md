---
title: CEIL (Lakehouse v2)
description: CEIL — zwraca najmniejszą liczbę całkowitą większą lub równą podanej liczbie.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/ceil.md
---

Zwraca najmniejszą liczbę całkowitą większą lub równą podanej liczbie.

## Składnia Analyze

```python
func.ceil(<x>)
```

## Przykłady Analyze

```python
func.ceil(3.2)

┌───┐
│ 4  │
└───┘
```

## Składnia SQL

```sql
CEIL(<x>)
```

## Przykłady SQL

```sql
SELECT CEIL(3.2);

┌───┐
│ 4  │
└───┘
```
