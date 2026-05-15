---
title: IS_FLOAT (Lakehouse v1)
description: IS_FLOAT — Checks if the input JSON value is a float.
---

Checks if the input JSON value is a float.

## Analyze Syntax

```python
func.is_float(<expr>)
```

## Analyze Examples

```python

func.is_float(func.parse_json('1.23')), func.is_float(func.parse_json('[1,2,3]'))
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ func.is_float(func.parse_json('1.23'))   │ func.is_float(func.parse_json('[1,2,3]'))   │
├──────────────────────────────────────────┼─────────────────────────────────────────────┤
│ true                                     │ false                                       │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

## SQL Syntax

```sql
IS_FLOAT( <expr> )
```

## Return Type

Returns `true` if the input JSON value is a float, and `false` otherwise.

## SQL Examples

```sql
SELECT
  IS_FLOAT(PARSE_JSON('1.23')),
  IS_FLOAT(PARSE_JSON('[1,2,3]'));

┌────────────────────────────────────────────────────────────────┐
│ is_float(parse_json('1.23')) │ is_float(parse_json('[1,2,3]')) │
├──────────────────────────────┼─────────────────────────────────┤
│ true                         │ false                           │
└────────────────────────────────────────────────────────────────┘
```
