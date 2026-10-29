---
title: LN (Lakehouse v2)
description: LN — zwraca logarytm naturalny liczby.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/ln.md
---

Zwraca logarytm naturalny liczby.

## Składnia Analyze

```python
func.ln(<x>)
```

## Przykłady Analyze

```python
func.ln(2.718281828459045)

┌─────┐
│ 1.0  │
└─────┘
```

## Składnia SQL

```sql
LN(<x>)
```

## Przykłady SQL

```sql
SELECT LN(EXP(1));

┌─────┐
│ 1.0  │
└─────┘
```
