---
title: SIN (Lakehouse v2)
description: SIN — zwraca sinus liczby w radianach.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/sin.md
---

Zwraca sinus liczby w radianach.

## Składnia Analyze

```python
func.sin(<x>)
```

## Przykłady Analyze

```python
func.sin(0)

┌─────┐
│ 0.0  │
└─────┘
```

## Składnia SQL

```sql
SIN(<x>)
```

## Przykłady SQL

```sql
SELECT SIN(0);

┌─────┐
│ 0.0  │
└─────┘
```
