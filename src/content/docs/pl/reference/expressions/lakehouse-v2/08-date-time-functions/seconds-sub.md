---
title: SECONDS_SUB (Lakehouse v2)
description: SECONDS_SUB — odejmuje określoną liczbę sekund od daty i godziny.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/seconds-sub.md
---

Odejmuje określoną liczbę sekund od daty i godziny.

## Składnia Analyze

```python
func.seconds_sub(<datetime>, <n>)
```

## Przykłady Analyze

```python
func.seconds_sub('2024-01-01 00:01:30', 90)

┌───────────────────────┐
│ '2024-01-01 00:00:00'  │
└───────────────────────┘
```

## Składnia SQL

```sql
SECONDS_SUB(<datetime>, <n>)
```

## Przykłady SQL

```sql
SELECT SECONDS_SUB('2024-01-01 00:01:30', 90);

┌─────────────────────┐
│ 2024-01-01 00:00:00  │
└─────────────────────┘
```
