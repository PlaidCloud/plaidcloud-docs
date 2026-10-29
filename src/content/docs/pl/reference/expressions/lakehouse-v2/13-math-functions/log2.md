---
title: LOG2 (Lakehouse v2)
description: LOG2 — zwraca logarytm przy podstawie 2 z liczby.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/log2.md
---

Zwraca logarytm przy podstawie 2 z liczby.

## Składnia Analyze

```python
func.log2(<x>)
```

## Przykłady Analyze

```python
func.log2(8)

┌─────┐
│ 3.0  │
└─────┘
```

## Składnia SQL

```sql
LOG2(<x>)
```

## Przykłady SQL

```sql
SELECT LOG2(8);

┌─────┐
│ 3.0  │
└─────┘
```
