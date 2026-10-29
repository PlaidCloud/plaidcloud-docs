---
title: WEEKS_DIFF (Lakehouse v2)
description: WEEKS_DIFF — zwraca liczbę tygodni między dwiema datami.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/weeks-diff.md
---

Zwraca liczbę tygodni między dwiema datami.

## Składnia Analyze

```python
func.weeks_diff(<end_date>, <start_date>)
```

## Przykłady Analyze

```python
func.weeks_diff('2024-03-01', '2024-01-01')

┌───┐
│ 8  │
└───┘
```

## Składnia SQL

```sql
WEEKS_DIFF(<end_date>, <start_date>)
```

## Przykłady SQL

```sql
SELECT WEEKS_DIFF('2024-03-01', '2024-01-01');

┌───┐
│ 8  │
└───┘
```
