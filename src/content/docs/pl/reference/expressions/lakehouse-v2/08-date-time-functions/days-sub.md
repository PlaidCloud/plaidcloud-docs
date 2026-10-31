---
title: DAYS_SUB (Lakehouse v2)
description: DAYS_SUB — odejmuje od daty podaną liczbę dni.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/days-sub.md
---

Odejmuje od daty podaną liczbę dni.

## Składnia Analyze

```python
func.days_sub(<date>, <n>)
```

## Przykłady Analyze

```python
func.days_sub('2024-01-31', 30)

┌──────────────┐
│ '2024-01-01'  │
└──────────────┘
```

## Składnia SQL

```sql
DAYS_SUB(<date>, <n>)
```

## Przykłady SQL

```sql
SELECT DAYS_SUB('2024-01-31', 30);

┌────────────┐
│ 2024-01-01  │
└────────────┘
```
