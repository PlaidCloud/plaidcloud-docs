---
title: POW (Lakehouse v2)
description: POW — zwraca liczbę podniesioną do potęgi o wykładniku równym drugiej liczbie.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/pow.md
---

Zwraca liczbę podniesioną do potęgi o wykładniku równym drugiej liczbie.

## Składnia Analyze

```python
func.pow(<x>, <y>)
```

## Przykłady Analyze

```python
func.pow(2, 10)

┌────────┐
│ 1024.0  │
└────────┘
```

## Składnia SQL

```sql
POW(<x>, <y>)
```

## Przykłady SQL

```sql
SELECT POW(2, 10);

┌────────┐
│ 1024.0  │
└────────┘
```
