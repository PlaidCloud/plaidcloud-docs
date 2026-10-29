---
title: TIMEDIFF (Lakehouse v2)
description: TIMEDIFF — zwraca różnicę między dwiema wartościami czasu.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/timediff.md
---

Zwraca różnicę między dwiema wartościami czasu.

## Składnia Analyze

```python
func.timediff(<time1>, <time2>)
```

## Przykłady Analyze

```python
func.timediff('15:30:00', '10:00:00')

┌────────────┐
│ '05:30:00'  │
└────────────┘
```

## Składnia SQL

```sql
TIMEDIFF(<time1>, <time2>)
```

## Przykłady SQL

```sql
SELECT TIMEDIFF('15:30:00', '10:00:00');

┌──────────┐
│ 05:30:00  │
└──────────┘
```
