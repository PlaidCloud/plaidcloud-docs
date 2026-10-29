---
title: LOG(x) (Lakehouse v1)
description: LOG(x) — zwraca logarytm naturalny z x.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/logx.md
---

Zwraca logarytm naturalny z `x`. Jeśli x jest mniejsze lub równe 0.0E0, funkcja zwraca NULL.

## Składnia Analyze

```python
 func.log( <x> )
```

## Przykłady Analyze

```python
 func.log(2)

┌────────────────────┐
│    func.log(2)     │
├────────────────────┤
│ 0.6931471805599453 │
└────────────────────┘
```

## Składnia SQL

```sql
LOG( <x> )
```

## Przykłady SQL

```sql
SELECT LOG(2);

┌────────────────────┐
│       log(2)       │
├────────────────────┤
│ 0.6931471805599453 │
└────────────────────┘
```
