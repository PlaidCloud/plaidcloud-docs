---
title: DATE_SUB (Lakehouse v2)
description: DATE_SUB — odejmuje od daty lub daty i godziny podany przedział czasu.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/date-sub.md
---

Odejmuje od daty lub daty i godziny podany przedział czasu.

## Składnia Analyze

```python
func.date_sub(<date>, INTERVAL <n> <unit>)
```

## Przykłady Analyze

```python
func.date_sub('2024-03-01', text('INTERVAL 1 MONTH'))

┌──────────────┐
│ '2024-02-01'  │
└──────────────┘
```

## Składnia SQL

```sql
DATE_SUB(<date>, INTERVAL <n> <unit>)
```

## Przykłady SQL

```sql
SELECT DATE_SUB('2024-03-01', INTERVAL 1 MONTH);

┌────────────┐
│ 2024-02-01  │
└────────────┘
```
