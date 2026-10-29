---
title: TIME_SLICE (Lakehouse v2)
description: TIME_SLICE — konwertuje podany czas na początek lub koniec przedziału czasu.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/time-slice.md
---

Konwertuje podany czas na początek lub koniec przedziału czasu.

## Składnia Analyze

```python
func.time_slice(<datetime>, INTERVAL <n> <unit>[, <boundary>])
```

## Przykłady Analyze

```python
func.time_slice('2024-06-15 14:35:00', text('INTERVAL 15 MINUTE'))

┌───────────────────────┐
│ '2024-06-15 14:30:00'  │
└───────────────────────┘
```

## Składnia SQL

```sql
TIME_SLICE(<datetime>, INTERVAL <n> <unit>[, <boundary>])
```

## Przykłady SQL

```sql
SELECT TIME_SLICE('2024-06-15 14:35:00', INTERVAL 15 MINUTE);

┌─────────────────────┐
│ 2024-06-15 14:30:00  │
└─────────────────────┘
```
