---
title: LOG10 (Lakehouse v2)
description: LOG10 — zwraca logarytm dziesiętny liczby.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/log10.md
---

Zwraca logarytm dziesiętny liczby.

## Składnia Analyze

```python
func.log10(<x>)
```

## Przykłady Analyze

```python
func.log10(1000)

┌─────┐
│ 3.0  │
└─────┘
```

## Składnia SQL

```sql
LOG10(<x>)
```

## Przykłady SQL

```sql
SELECT LOG10(1000);

┌─────┐
│ 3.0  │
└─────┘
```
