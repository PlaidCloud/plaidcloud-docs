---
title: MINUTES_SUB (Lakehouse v2)
description: MINUTES_SUB — odejmuje określoną liczbę minut od daty i godziny.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/minutes-sub.md
---

Odejmuje określoną liczbę minut od daty i godziny.

## Składnia Analyze

```python
func.minutes_sub(<datetime>, <n>)
```

## Przykłady Analyze

```python
func.minutes_sub('2024-01-01 10:45:00', 45)

┌───────────────────────┐
│ '2024-01-01 10:00:00'  │
└───────────────────────┘
```

## Składnia SQL

```sql
MINUTES_SUB(<datetime>, <n>)
```

## Przykłady SQL

```sql
SELECT MINUTES_SUB('2024-01-01 10:45:00', 45);

┌─────────────────────┐
│ 2024-01-01 10:00:00  │
└─────────────────────┘
```
