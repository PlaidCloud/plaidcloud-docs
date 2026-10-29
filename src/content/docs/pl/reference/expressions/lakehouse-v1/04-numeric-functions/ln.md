---
title: LN (Lakehouse v1)
description: LN — zwraca logarytm naturalny z x, czyli logarytm o podstawie e z x.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/ln.md
---

Zwraca logarytm naturalny z `x`, czyli logarytm o podstawie e z `x`. Jeśli x jest mniejsze lub równe 0.0E0, funkcja zwraca NULL.

## Składnia Analyze

```python
func.ln( <x> )
```

## Przykłady Analyze

```python
func.ln(2)

┌────────────────────┐
│     func.ln(2)     │
├────────────────────┤
│ 0.6931471805599453 │
└────────────────────┘
```

## Składnia SQL

```sql
LN( <x> )
```

## Przykłady SQL

```sql
SELECT LN(2);

┌────────────────────┐
│        ln(2)       │
├────────────────────┤
│ 0.6931471805599453 │
└────────────────────┘
```
