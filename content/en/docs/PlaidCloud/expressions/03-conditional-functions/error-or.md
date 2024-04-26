---
title: ERROR_OR
---

Returns the first non-error expression among its inputs. If all expressions result in errors, it returns NULL.

## Analyze Syntax

```python
func.error_or(expr1, expr2, ...)
```

## Analyze Examples

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

## SQL Syntax

```sql
ERROR_OR(expr1, expr2, ...)
```

## SQL Examples

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