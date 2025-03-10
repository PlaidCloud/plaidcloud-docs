---
title: IS_ERROR
---

Returns a Boolean value indicating whether an expression is an error value.

See also: [IS_NOT_ERROR](../is-not-error)

## Analyze Syntax

```python
func.is_error( <expr> )
```

## Analyze Examples

```python
# Indicates division by zero, hence an error
func.is_error((1 / 0)), func.is_not_error((1 / 0))

┌─────────────────────────────────────────────────────┐
│ func.is_error((1 / 0)) │ func.is_not_error((1 / 0)) │
├────────────────────────┼────────────────────────────┤
│ true                   │ false                      │
└─────────────────────────────────────────────────────┘

# The conversion to DATE is successful, hence not an error
func.is_error(func.to_date('2024-03-17')), func.is_not_error(func.to_date('2024-03-17'))

┌───────────────────────────────────────────────────────────────────────────────────────────┐
│ func.is_error(func.to_date('2024-03-17')) │ func.is_not_error(func.to_date('2024-03-17')) │
├───────────────────────────────────────────┼───────────────────────────────────────────────┤
│ false                                     │ true                                          │
└───────────────────────────────────────────────────────────────────────────────────────────┘
```

## SQL Syntax

```sql
IS_ERROR( <expr> )
```

## Return Type

Returns `true` if the expression is an error, otherwise `false`.

## SQL Examples

```sql
-- Indicates division by zero, hence an error
SELECT IS_ERROR(1/0), IS_NOT_ERROR(1/0);

┌───────────────────────────────────────────┐
│ is_error((1 / 0)) │ is_not_error((1 / 0)) │
├───────────────────┼───────────────────────┤
│ true              │ false                 │
└───────────────────────────────────────────┘

-- The conversion to DATE is successful, hence not an error
SELECT IS_ERROR('2024-03-17'::DATE), IS_NOT_ERROR('2024-03-17'::DATE);

┌─────────────────────────────────────────────────────────────────┐
│ is_error('2024-03-17'::date) │ is_not_error('2024-03-17'::date) │
├──────────────────────────────┼──────────────────────────────────┤
│ false                        │ true                             │
└─────────────────────────────────────────────────────────────────┘
```