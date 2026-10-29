---
title: MONTH (Lakehouse v2)
description: MONTH — zwraca miesiąc z daty.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/month.md
---

Zwraca miesiąc z daty.

## Składnia Analyze

```python
func.month(<date>)
```

## Przykłady Analyze

```python
func.month('2024-06-15')

┌───┐
│ 6  │
└───┘
```

## Składnia SQL

```sql
MONTH(<date>)
```

## Przykłady SQL

```sql
SELECT MONTH('2024-06-15');

┌───┐
│ 6  │
└───┘
```
