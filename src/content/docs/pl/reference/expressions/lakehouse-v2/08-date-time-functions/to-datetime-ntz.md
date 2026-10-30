---
title: TO_DATETIME_NTZ (Lakehouse v2)
description: TO_DATETIME_NTZ — konwertuje wartość na DATETIME bez strefy czasowej (NTZ).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/to-datetime-ntz.md
---

Konwertuje wartość na DATETIME bez strefy czasowej (NTZ). Na wynik nie wpływają ustawienia strefy czasowej sesji.

## Składnia Analyze

```python
func.to_datetime_ntz('2024-06-15 14:30:00')
```

## Przykłady Analyze

```python
func.to_datetime_ntz('2024-06-15 14:30:00')

┌─────────────────────┐
│ 2024-06-15 14:30:00 │
└─────────────────────┘
```

## Składnia SQL

```sql
TO_DATETIME_NTZ(<expr>)
```

## Przykłady SQL

```sql
SELECT TO_DATETIME_NTZ('2024-06-15 14:30:00');

┌─────────────────────┐
│ 2024-06-15 14:30:00 │
└─────────────────────┘
```
