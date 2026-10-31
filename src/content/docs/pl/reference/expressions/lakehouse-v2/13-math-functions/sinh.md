---
title: SINH (Lakehouse v2)
description: SINH — zwraca sinus hiperboliczny liczby.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/sinh.md
---

Zwraca sinus hiperboliczny liczby.

## Składnia Analyze

```python
func.sinh(<x>)
```

## Przykłady Analyze

```python
func.sinh(0)

┌─────┐
│ 0.0  │
└─────┘
```

## Składnia SQL

```sql
SINH(<x>)
```

## Przykłady SQL

```sql
SELECT SINH(0);

┌─────┐
│ 0.0  │
└─────┘
```
