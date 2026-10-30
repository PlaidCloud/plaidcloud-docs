---
title: DAYOFMONTH (Lakehouse v2)
description: DAYOFMONTH — zwraca dzień miesiąca z daty. Alias funkcji `DAY`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/dayofmonth.md
---

Zwraca dzień miesiąca z daty. Alias funkcji `DAY`.

## Składnia Analyze

```python
func.dayofmonth(<date>)
```

## Przykłady Analyze

```python
func.dayofmonth('2024-06-15')

┌────┐
│ 15  │
└────┘
```

## Składnia SQL

```sql
DAYOFMONTH(<date>)
```

## Przykłady SQL

```sql
SELECT DAYOFMONTH('2024-06-15');

┌────┐
│ 15  │
└────┘
```
