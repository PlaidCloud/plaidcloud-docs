---
title: MONTHNAME (Lakehouse v2)
description: MONTHNAME — zwraca nazwę miesiąca dla daty.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/monthname.md
---

Zwraca nazwę miesiąca dla daty.

## Składnia Analyze

```python
func.monthname(<date>)
```

## Przykłady Analyze

```python
func.monthname('2024-06-15')

┌────────┐
│ 'June'  │
└────────┘
```

## Składnia SQL

```sql
MONTHNAME(<date>)
```

## Przykłady SQL

```sql
SELECT MONTHNAME('2024-06-15');

┌──────┐
│ June  │
└──────┘
```
