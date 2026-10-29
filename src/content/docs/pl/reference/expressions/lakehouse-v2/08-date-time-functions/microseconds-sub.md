---
title: MICROSECONDS_SUB (Lakehouse v2)
description: MICROSECONDS_SUB — odejmuje określoną liczbę mikrosekund od daty i godziny.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/microseconds-sub.md
---

Odejmuje określoną liczbę mikrosekund od daty i godziny.

## Składnia Analyze

```python
func.microseconds_sub(<datetime>, <n>)
```

## Przykłady Analyze

```python
func.microseconds_sub('2024-01-01 00:00:01', 1000000)

┌───────────────────────┐
│ '2024-01-01 00:00:00'  │
└───────────────────────┘
```

## Składnia SQL

```sql
MICROSECONDS_SUB(<datetime>, <n>)
```

## Przykłady SQL

```sql
SELECT MICROSECONDS_SUB('2024-01-01 00:00:01', 1000000);

┌─────────────────────┐
│ 2024-01-01 00:00:00  │
└─────────────────────┘
```
