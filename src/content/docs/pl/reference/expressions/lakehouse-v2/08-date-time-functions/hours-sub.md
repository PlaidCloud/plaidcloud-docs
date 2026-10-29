---
title: HOURS_SUB (Lakehouse v2)
description: HOURS_SUB — odejmuje od daty i godziny podaną liczbę godzin.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/hours-sub.md
---

Odejmuje od daty i godziny podaną liczbę godzin.

## Składnia Analyze

```python
func.hours_sub(<datetime>, <n>)
```

## Przykłady Analyze

```python
func.hours_sub('2024-01-01 15:00:00', 5)

┌───────────────────────┐
│ '2024-01-01 10:00:00'  │
└───────────────────────┘
```

## Składnia SQL

```sql
HOURS_SUB(<datetime>, <n>)
```

## Przykłady SQL

```sql
SELECT HOURS_SUB('2024-01-01 15:00:00', 5);

┌─────────────────────┐
│ 2024-01-01 10:00:00  │
└─────────────────────┘
```
