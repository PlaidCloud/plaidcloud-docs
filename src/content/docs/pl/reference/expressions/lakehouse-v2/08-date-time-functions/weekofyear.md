---
title: WEEKOFYEAR (Lakehouse v2)
description: WEEKOFYEAR — zwraca tydzień roku dla daty. Alias funkcji `WEEK`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/weekofyear.md
---

Zwraca tydzień roku dla daty. Alias funkcji `WEEK`.

## Składnia Analyze

```python
func.weekofyear(<date>)
```

## Przykłady Analyze

```python
func.weekofyear('2024-06-15')

┌────┐
│ 24  │
└────┘
```

## Składnia SQL

```sql
WEEKOFYEAR(<date>)
```

## Przykłady SQL

```sql
SELECT WEEKOFYEAR('2024-06-15');

┌────┐
│ 24  │
└────┘
```
