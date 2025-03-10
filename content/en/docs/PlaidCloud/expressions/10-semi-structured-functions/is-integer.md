---
title: IS_INTEGER
---

Checks if the input JSON value is an integer.


## Analyze Syntax

```python
func.is_integer(<expr>)
```

## Analyze Example

```python

func.is_integer(func.parse_json('123')), func.is_integer(func.parse_json('[1,2,3]'))
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ func.is_integer(func.parse_json('123'))  │ func.is_integer(func.parse_json('[1,2,3]')) │
├──────────────────────────────────────────┼─────────────────────────────────────────────┤
│ true                                     │ false                                       │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

## SQL Syntax

```sql
IS_INTEGER( <expr> )
```

## Return Type

Returns `true` if the input JSON value is an integer, and `false` otherwise.

## SQL Examples

```sql
SELECT
  IS_INTEGER(PARSE_JSON('123')),
  IS_INTEGER(PARSE_JSON('[1,2,3]'));

┌───────────────────────────────────────────────────────────────────┐
│ is_integer(parse_json('123')) │ is_integer(parse_json('[1,2,3]')) │
├───────────────────────────────┼───────────────────────────────────┤
│ true                          │ false                             │
└───────────────────────────────────────────────────────────────────┘
```