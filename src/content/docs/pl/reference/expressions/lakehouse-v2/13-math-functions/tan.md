---
title: TAN (Lakehouse v2)
description: TAN — zwraca tangens liczby w radianach.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/tan.md
---

Zwraca tangens liczby w radianach.

## Składnia Analyze

```python
func.tan(<x>)
```

## Przykłady Analyze

```python
func.tan(0)

┌─────┐
│ 0.0  │
└─────┘
```

## Składnia SQL

```sql
TAN(<x>)
```

## Przykłady SQL

```sql
SELECT TAN(0);

┌─────┐
│ 0.0  │
└─────┘
```
