---
title: DATE_SLICE (Lakehouse v2)
description: "Użyj funkcji daty i czasu DATE_SLICE w PlaidCloud Lakehouse. Przekształca podany czas na początek lub koniec przedziału czasu na podstawie określonego okresu."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/date-slice.md
---

Przekształca podany czas na początek lub koniec przedziału czasu na podstawie określonego okresu.

## Składnia Analyze

```python
func.date_slice(<datetime>, INTERVAL <n> <unit>[, <boundary>])
```

## Przykłady Analyze

```python
func.date_slice('2024-06-15 14:35:00', text('INTERVAL 1 HOUR'))

┌───────────────────────┐
│ '2024-06-15 14:00:00'  │
└───────────────────────┘
```

## Składnia SQL

```sql
DATE_SLICE(<datetime>, INTERVAL <n> <unit>[, <boundary>])
```

## Przykłady SQL

```sql
SELECT DATE_SLICE('2024-06-15 14:35:00', INTERVAL 1 HOUR);

┌─────────────────────┐
│ 2024-06-15 14:00:00  │
└─────────────────────┘
```
