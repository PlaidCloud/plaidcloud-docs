---
title: DAYOFYEAR (Lakehouse v2)
description: DAYOFYEAR — zwraca dzień roku z daty.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/dayofyear.md
---

Zwraca dzień roku z daty.

## Składnia Analyze

```python
func.dayofyear(<date>)
```

## Przykłady Analyze

```python
func.dayofyear('2024-06-15')

┌─────┐
│ 167  │
└─────┘
```

## Składnia SQL

```sql
DAYOFYEAR(<date>)
```

## Przykłady SQL

```sql
SELECT DAYOFYEAR('2024-06-15');

┌─────┐
│ 167  │
└─────┘
```
