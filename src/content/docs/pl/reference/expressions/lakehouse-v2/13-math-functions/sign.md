---
title: SIGN (Lakehouse v2)
description: "SIGN — zwraca znak liczby: -1, 0 lub 1."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/sign.md
---

Zwraca znak liczby: -1, 0 lub 1.

## Składnia Analyze

```python
func.sign(<x>)
```

## Przykłady Analyze

```python
func.sign(-42)

┌────┐
│ -1  │
└────┘
```

## Składnia SQL

```sql
SIGN(<x>)
```

## Przykłady SQL

```sql
SELECT SIGN(-42);

┌────┐
│ -1  │
└────┘
```
