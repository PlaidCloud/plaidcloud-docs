---
title: MONTHS_SUB (Lakehouse v2)
description: MONTHS_SUB — odejmuje określoną liczbę miesięcy od daty.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/months-sub.md
---

Odejmuje określoną liczbę miesięcy od daty.

## Składnia Analyze

```python
func.months_sub(<date>, <n>)
```

## Przykłady Analyze

```python
func.months_sub('2024-06-15', 3)

┌──────────────┐
│ '2024-03-15'  │
└──────────────┘
```

## Składnia SQL

```sql
MONTHS_SUB(<date>, <n>)
```

## Przykłady SQL

```sql
SELECT MONTHS_SUB('2024-06-15', 3);

┌────────────┐
│ 2024-03-15  │
└────────────┘
```
