---
title: ASSUME_NOT_NULL
---

Results in an equivalent non-`Nullable` value for a Nullable type. In case the original value is `NULL` the result is undetermined. 

## Analyze Syntax

```python
func.assume_not_null(<x>)
```

## Analyze Examples

```python
With a table like:

┌────────────────────┐
│        x  │   y    │
├────────────────────┤
│         1 │   NULL │
│         2 │      3 │
└────────────────────┘

func.assume_not_null(y)
┌─────────────────────────┐
│ func.assume_not_null(y) │
├─────────────────────────┤
│                       0 │
│                       3 │
└─────────────────────────┘
```

## SQL Syntax

```sql
ASSUME_NOT_NULL(<x>)
```

## Aliases

- [REMOVE_NULLABLE](../remove-nullable)

## Return Type

Returns the original datatype from the non-`Nullable` type; Returns the embedded non-`Nullable` datatype for `Nullable` type.

## SQL Examples

```sql
CREATE TABLE default.t_null ( x int,  y int null);

INSERT INTO default.t_null values (1, null), (2, 3);

SELECT ASSUME_NOT_NULL(y), REMOVE_NULLABLE(y) FROM t_null;

┌─────────────────────────────────────────┐
│ assume_not_null(y) │ remove_nullable(y) │
├────────────────────┼────────────────────┤
│                  0 │                  0 │
│                  3 │                  3 │
└─────────────────────────────────────────┘
```