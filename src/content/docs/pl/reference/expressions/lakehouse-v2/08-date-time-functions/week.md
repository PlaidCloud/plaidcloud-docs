---
title: WEEK (Lakehouse v2)
description: WEEK — zwraca numer tygodnia w roku dla daty.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/week.md
---

Zwraca numer tygodnia w roku dla daty.

## Składnia Analyze

```python
func.week(<date>[, <mode>])
```

## Przykłady Analyze

```python
func.week('2024-06-15')

┌────┐
│ 24  │
└────┘
```

## Składnia SQL

```sql
WEEK(<date>[, <mode>])
```

## Przykłady SQL

```sql
SELECT WEEK('2024-06-15');

┌────┐
│ 24  │
└────┘
```
