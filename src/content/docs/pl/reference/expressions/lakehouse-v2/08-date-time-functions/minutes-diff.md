---
title: MINUTES_DIFF (Lakehouse v2)
description: MINUTES_DIFF — zwraca liczbę minut między dwiema datami i godzinami.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/minutes-diff.md
---

Zwraca liczbę minut między dwiema datami i godzinami.

## Składnia Analyze

```python
func.minutes_diff(<end>, <start>)
```

## Przykłady Analyze

```python
func.minutes_diff('2024-01-01 11:00:00', '2024-01-01 10:00:00')

┌────┐
│ 60  │
└────┘
```

## Składnia SQL

```sql
MINUTES_DIFF(<end>, <start>)
```

## Przykłady SQL

```sql
SELECT MINUTES_DIFF('2024-01-01 11:00:00', '2024-01-01 10:00:00');

┌────┐
│ 60  │
└────┘
```
