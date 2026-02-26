---
title: TO_QUARTER
---

Retrieves the quarter (1, 2, 3, or 4) from a given date or timestamp.

## Analyze Syntax

```python
func.to_quarter(<expr>)
```

## Analyze Examples

```python
func.now(), func.to_quarter(func.now()), func.quarter(func.now())

┌─────────────────────────────────────────────────────────────────────────────────────┐
│       func.now()           │ func.to_quarter(func.now()) │ func.quarter(func.now()) │
├────────────────────────────┼─────────────────────────────┼──────────────────────────┤
│ 2024-03-14 23:32:52.743133 │                           3 │                        3 │
└─────────────────────────────────────────────────────────────────────────────────────┘
```

## SQL Syntax

```sql
TO_QUARTER( <date_or_time_expr> )
```

## Aliases

- [QUARTER](quarter)

## Return Type

Integer.

## SQL Examples

```sql
SELECT NOW(), TO_QUARTER(NOW()), QUARTER(NOW());

┌─────────────────────────────────────────────────────────────────┐
│            now()           │ to_quarter(now()) │ quarter(now()) │
├────────────────────────────┼───────────────────┼────────────────┤
│ 2024-03-14 23:32:52.743133 │                 1 │              1 │
└─────────────────────────────────────────────────────────────────┘
```