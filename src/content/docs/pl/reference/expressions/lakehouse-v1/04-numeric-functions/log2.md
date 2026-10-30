---
title: LOG2 (Lakehouse v1)
description: LOG2 — zwraca logarytm binarny z x.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/log2.md
---

Zwraca logarytm o podstawie 2 z `x`. Jeśli `x` jest mniejsze lub równe 0.0E0, funkcja zwraca NULL.

## Składnia Analyze

```python
func.log2( <x> )
```

## Przykłady Analyze

```python
func.log2(65536)

┌──────────────────┐
│ func.log2(65536) │
├──────────────────┤
│               16 │
└──────────────────┘
```

## Składnia SQL

```sql
LOG2( <x> )
```

## Przykłady SQL

```sql
SELECT LOG2(65536);

┌─────────────┐
│ log2(65536) │
├─────────────┤
│          16 │
└─────────────┘
```
