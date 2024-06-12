---
title: IS_OBJECT
---

Checks if the input value is a JSON object.

## Analyze Syntax

```python
func.is_object(<expr>)
```

## Analyze Example

```python

func.is_object(func.parse_json('{"a":"b"}')), func.is_object(func.parse_json('["a","b","c"]'))
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│ func.is_object(func.parse_json('{"a":"b"}'))  │ func.is_object(func.parse_json('["a","b","c"]')) │
├───────────────────────────────────────────────┼──────────────────────────────────────────────────┤
│ true                                          │ false                                            │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
```

## SQL Syntax

```sql
IS_OBJECT( <expr> )
```

## Return Type

Returns `true` if the input JSON value is a JSON object, and `false` otherwise.

## SQL Examples

```sql
SELECT
  IS_OBJECT(PARSE_JSON('{"a":"b"}')), -- JSON Object
  IS_OBJECT(PARSE_JSON('["a","b","c"]')); --JSON Array

┌─────────────────────────────────────────────────────────────────────────────┐
│ is_object(parse_json('{"a":"b"}')) │ is_object(parse_json('["a","b","c"]')) │
├────────────────────────────────────┼────────────────────────────────────────┤
│ true                               │ false                                  │
└─────────────────────────────────────────────────────────────────────────────┘
```