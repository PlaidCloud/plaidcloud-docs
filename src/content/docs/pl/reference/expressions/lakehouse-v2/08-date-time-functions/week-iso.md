---
title: WEEK_ISO (Lakehouse v2)
description: WEEK_ISO — zwraca numer tygodnia ISO w roku dla daty.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/week-iso.md
---

Zwraca numer tygodnia ISO w roku dla daty.

## Składnia Analyze

```python
func.week_iso(<date>)
```

## Przykłady Analyze

```python
func.week_iso('2024-06-15')

┌────┐
│ 24  │
└────┘
```

## Składnia SQL

```sql
WEEK_ISO(<date>)
```

## Przykłady SQL

```sql
SELECT WEEK_ISO('2024-06-15');

┌────┐
│ 24  │
└────┘
```
