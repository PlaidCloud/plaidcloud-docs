---
title: DAY (Lakehouse v2)
description: DAY — zwraca dzień miesiąca z daty.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/day.md
---

Zwraca dzień miesiąca z daty.

## Składnia Analyze

```python
func.day(<date>)
```

## Przykłady Analyze

```python
func.day('2024-06-15')

┌────┐
│ 15  │
└────┘
```

## Składnia SQL

```sql
DAY(<date>)
```

## Przykłady SQL

```sql
SELECT DAY('2024-06-15');

┌────┐
│ 15  │
└────┘
```
