---
title: "LOG(b, x) (Lakehouse v1)"
description: LOG(b, x) — zwraca logarytm o podstawie b z x.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/logbx.md
---

Zwraca logarytm o podstawie b z `x`. Jeśli `x` jest mniejsze lub równe 0.0E0, funkcja zwraca NULL.

## Składnia Analyze

```python
func.log( <b, x> )
```

## Przykłady Analyze

```python
func.log(2, 65536)

┌────────────────────┐
│ func.log(2, 65536) │
├────────────────────┤
│                 16 │
└────────────────────┘
```

## Składnia SQL

```sql
LOG( <b, x> )
```

## Przykłady SQL

```sql
SELECT LOG(2, 65536);

┌───────────────┐
│ log(2, 65536) │
├───────────────┤
│            16 │
└───────────────┘
```
