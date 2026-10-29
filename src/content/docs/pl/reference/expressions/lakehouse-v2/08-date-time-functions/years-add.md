---
title: YEARS_ADD (Lakehouse v2)
description: YEARS_ADD — dodaje określoną liczbę lat do daty.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/years-add.md
---

Dodaje określoną liczbę lat do daty.

## Składnia Analyze

```python
func.years_add(<date>, <n>)
```

## Przykłady Analyze

```python
func.years_add('2024-01-01', 5)

┌──────────────┐
│ '2029-01-01'  │
└──────────────┘
```

## Składnia SQL

```sql
YEARS_ADD(<date>, <n>)
```

## Przykłady SQL

```sql
SELECT YEARS_ADD('2024-01-01', 5);

┌────────────┐
│ 2029-01-01  │
└────────────┘
```
