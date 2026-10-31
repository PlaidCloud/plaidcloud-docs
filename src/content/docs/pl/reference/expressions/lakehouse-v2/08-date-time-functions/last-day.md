---
title: LAST_DAY (Lakehouse v2)
description: LAST_DAY — zwraca ostatni dzień miesiąca dla podanej daty.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/last-day.md
---

Zwraca ostatni dzień miesiąca dla podanej daty.

## Składnia Analyze

```python
func.last_day(<date>[, <unit>])
```

## Przykłady Analyze

```python
func.last_day('2024-02-15')

┌──────────────┐
│ '2024-02-29'  │
└──────────────┘
```

## Składnia SQL

```sql
LAST_DAY(<date>[, <unit>])
```

## Przykłady SQL

```sql
SELECT LAST_DAY('2024-02-15');

┌────────────┐
│ 2024-02-29  │
└────────────┘
```
