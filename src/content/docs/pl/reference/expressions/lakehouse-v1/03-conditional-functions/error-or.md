---
title: ERROR_OR (Lakehouse v1)
description: ERROR_OR — zwraca pierwsze wyrażenie niebędące błędem spośród swoich argumentów.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/error-or.md
---

Zwraca pierwsze wyrażenie niebędące błędem spośród swoich argumentów. Jeśli wszystkie wyrażenia kończą się błędem, zwraca NULL.

## Składnia Analyze

```python
func.error_or(expr1, expr2, ...)
```

## Przykłady Analyze

```python
# Returns the valid date if no errors occur
# Returns the current date if the conversion results in an error
func.now(), func.error_or(func.to_date('2024-12-25'), func.now())

┌──────────────────────────────────────────────────────────────────────────────────────────┐
│            func.now()           │ func.error_or(func.to_date('2024-12-25'), func.now())  │
├─────────────────────────────────┼────────────────────────────────────────────────────────┤
│ 2024-03-18 01:22:39.460320      │ 2024-12-25                                             │
└──────────────────────────────────────────────────────────────────────────────────────────┘

# Returns NULL because the conversion results in an error
func.error_or(func.to_date('2024-1234'))

┌────────────────────────────────────────────┐
│ func.error_or(func.to_date('2024-1234'))   │
├────────────────────────────────────────────┤
│ NULL                                       │
└────────────────────────────────────────────┘
```

## Składnia SQL

```sql
ERROR_OR(expr1, expr2, ...)
```

## Przykłady SQL

```sql
-- Returns the valid date if no errors occur
-- Returns the current date if the conversion results in an error
SELECT NOW(), ERROR_OR('2024-12-25'::DATE, NOW()::DATE);

┌────────────────────────────────────────────────────────────────────────┐
│            now()           │ error_or('2024-12-25'::date, now()::date) │
├────────────────────────────┼───────────────────────────────────────────┤
│ 2024-03-18 01:22:39.460320 │ 2024-12-25                                │
└────────────────────────────────────────────────────────────────────────┘

-- Returns NULL because the conversion results in an error
SELECT ERROR_OR('2024-1234'::DATE);

┌─────────────────────────────┐
│ error_or('2024-1234'::date) │
├─────────────────────────────┤
│ NULL                        │
└─────────────────────────────┘
```
