---
title: COSH (Lakehouse v2)
description: COSH — zwraca cosinus hiperboliczny liczby.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/cosh.md
---

Zwraca cosinus hiperboliczny liczby.

## Składnia Analyze

```python
func.cosh(<x>)
```

## Przykłady Analyze

```python
func.cosh(0)

┌─────┐
│ 1.0  │
└─────┘
```

## Składnia SQL

```sql
COSH(<x>)
```

## Przykłady SQL

```sql
SELECT COSH(0);

┌─────┐
│ 1.0  │
└─────┘
```
