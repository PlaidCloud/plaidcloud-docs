---
title: TO_WEEK_OF_YEAR
---

Calculates the week number within a year for a given date.

ISO week numbering works as follows: January 4th is always considered part of the first week. If January 1st is a Thursday, then the week that spans from Monday, December 29th, to Sunday, January 4th, is designated as ISO week 1. If January 1st falls on a Friday, then the week that goes from Monday, January 4th, to Sunday, January 10th, is marked as ISO week 1.

## Analyze Syntax

```python
func.to_week_of_year(<expr>)
```

## Analyze Examples

```python
func.now(), func.to_week_of_year(func.now()), func.week(func.now()), func.weekofyear(func.now())

┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│       func.now()           │ func.to_week_of_year(func.now()) │ func.week(func.now()) │ func.weekofyear(func.now()) │
├────────────────────────────┼──────────────────────────────────┼───────────────────────┼─────────────────────────────┤
│ 2024-03-14 23:30:04.011624 │                               11 │                    11 │                          11 │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

## SQL Syntax

```sql
TO_WEEK_OF_YEAR(<expr>)
```

## Arguments

| Arguments | Description    |
|-----------|----------------|
| `<expr>`  | date/timestamp |

## Aliases

- [WEEK](week)
- [WEEKOFYEAR](weekofyear)

## Return Type

Returns an integer that represents the week number within a year, with numbering ranging from 1 to 53.

## SQL Examples

```sql
SELECT NOW(), TO_WEEK_OF_YEAR(NOW()), WEEK(NOW()), WEEKOFYEAR(NOW());

┌───────────────────────────────────────────────────────────────────────────────────────┐
│            now()           │ to_week_of_year(now()) │ week(now()) │ weekofyear(now()) │
├────────────────────────────┼────────────────────────┼─────────────┼───────────────────┤
│ 2024-03-14 23:30:04.011624 │                     11 │          11 │                11 │
└───────────────────────────────────────────────────────────────────────────────────────┘
```