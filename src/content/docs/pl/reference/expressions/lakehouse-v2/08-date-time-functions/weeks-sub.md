---
title: WEEKS_SUB (Lakehouse v2)
description: WEEKS_SUB — odejmuje określoną liczbę tygodni od daty.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/weeks-sub.md
---

Odejmuje określoną liczbę tygodni od daty.

## Składnia Analyze

```python
func.weeks_sub(<date>, <n>)
```

## Przykłady Analyze

```python
func.weeks_sub('2024-01-15', 2)

┌──────────────┐
│ '2024-01-01'  │
└──────────────┘
```

## Składnia SQL

```sql
WEEKS_SUB(<date>, <n>)
```

## Przykłady SQL

```sql
SELECT WEEKS_SUB('2024-01-15', 2);

┌────────────┐
│ 2024-01-01  │
└────────────┘
```
