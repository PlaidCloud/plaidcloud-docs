---
title: IS_STRING
---

Checks if the input JSON value is a string.

## Analyze Syntax

```python
func.is_string(<expr>)
```

## Analyze Example

```python

func.is_string(func.parse_json('"abc"')), func.is_string(func.parse_json('123'))
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│ func.is_string(func.parse_json('"abc"'))      │ func.is_string(func.parse_json('123'))           │
├───────────────────────────────────────────────┼──────────────────────────────────────────────────┤
│ true                                          │ false                                            │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
```

## SQL Syntax

```sql
IS_STRING( <expr> )
```

## Return Type

Returns `true` if the input JSON value is a string, and `false` otherwise.

## SQL Examples

```sql
SELECT
  IS_STRING(PARSE_JSON('"abc"')),
  IS_STRING(PARSE_JSON('123'));

┌───────────────────────────────────────────────────────────────┐
│ is_string(parse_json('"abc"')) │ is_string(parse_json('123')) │
├────────────────────────────────┼──────────────────────────────┤
│ true                           │ false                        │
└───────────────────────────────────────────────────────────────┘
```