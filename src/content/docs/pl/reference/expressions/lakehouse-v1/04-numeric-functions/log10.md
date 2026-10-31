---
title: LOG10 (Lakehouse v1)
description: LOG10 — zwraca logarytm dziesiętny z x. Dokumentacja referencyjna.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/log10.md
---

Zwraca logarytm dziesiętny z `x`. Jeśli `x` jest mniejsze lub równe 0.0E0, funkcja zwraca NULL.


## Składnia Analyze

```python
func.log10( <x> )
```

## Przykłady Analyze

```python
func.log10(100)

┌─────────────────┐
│ func.log10(100) │
├─────────────────┤
│               2 │
└─────────────────┘
```

## Składnia SQL

```sql
LOG10( <x> )
```

## Przykłady SQL

```sql
SELECT LOG10(100);

┌────────────┐
│ log10(100) │
├────────────┤
│          2 │
└────────────┘
```
