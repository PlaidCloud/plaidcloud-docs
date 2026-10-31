---
title: TANH (Lakehouse v2)
description: TANH — zwraca tangens hiperboliczny liczby.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/tanh.md
---

Zwraca tangens hiperboliczny liczby.

## Składnia Analyze

```python
func.tanh(<x>)
```

## Przykłady Analyze

```python
func.tanh(0)

┌─────┐
│ 0.0  │
└─────┘
```

## Składnia SQL

```sql
TANH(<x>)
```

## Przykłady SQL

```sql
SELECT TANH(0);

┌─────┐
│ 0.0  │
└─────┘
```
