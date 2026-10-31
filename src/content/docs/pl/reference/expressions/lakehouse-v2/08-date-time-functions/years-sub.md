---
title: YEARS_SUB (Lakehouse v2)
description: YEARS_SUB — odejmuje określoną liczbę lat od daty.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/years-sub.md
---

Odejmuje określoną liczbę lat od daty.

## Składnia Analyze

```python
func.years_sub(<date>, <n>)
```

## Przykłady Analyze

```python
func.years_sub('2029-01-01', 5)

┌──────────────┐
│ '2024-01-01'  │
└──────────────┘
```

## Składnia SQL

```sql
YEARS_SUB(<date>, <n>)
```

## Przykłady SQL

```sql
SELECT YEARS_SUB('2029-01-01', 5);

┌────────────┐
│ 2024-01-01  │
└────────────┘
```
