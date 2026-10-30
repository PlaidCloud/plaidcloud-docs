---
title: HOURS_DIFF (Lakehouse v2)
description: HOURS_DIFF — zwraca liczbę godzin między dwiema wartościami daty i godziny.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/hours-diff.md
---

Zwraca liczbę godzin między dwiema wartościami daty i godziny.

## Składnia Analyze

```python
func.hours_diff(<end>, <start>)
```

## Przykłady Analyze

```python
func.hours_diff('2024-01-02 10:00:00', '2024-01-01 10:00:00')

┌────┐
│ 24  │
└────┘
```

## Składnia SQL

```sql
HOURS_DIFF(<end>, <start>)
```

## Przykłady SQL

```sql
SELECT HOURS_DIFF('2024-01-02 10:00:00', '2024-01-01 10:00:00');

┌────┐
│ 24  │
└────┘
```
