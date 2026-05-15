---
title: PARSE_JSON
description: Interprets input JSON string, producing a VARIANT value
---

`parse_json` and `try_parse_json` interprets an input string as a JSON document, producing a VARIANT value.

`try_parse_json` returns a NULL value if an error occurs during parsing.

## Analyze Syntax

```python
func.parse_json(<json_string>)

or

func.try_parse_json(<json_string>)
```

## Analyze Examples

```python
func.parse_json('[-1, 12, 289, 2188, false]')

┌───────────────────────────────────────────────┐
│ func.parse_json('[-1, 12, 289, 2188, false]') │
├───────────────────────────────────────────────┤
│ [-1,12,289,2188,false]                        │
└───────────────────────────────────────────────┘

func.try_parse_json('{ "x" : "abc", "y" : false, "z": 10} ')

┌──────────────────────────────────────────────────────────────┐
│ func.try_parse_json('{ "x" : "abc", "y" : false, "z": 10} ') │
├──────────────────────────────────────────────────────────────┤
│ {"x":"abc","y":false,"z":10}                                 │
└──────────────────────────────────────────────────────────────┘
```

## SQL Syntax

```sql
PARSE_JSON(<expr>)
TRY_PARSE_JSON(<expr>)
```

## Arguments

| Arguments | Description                                                                    |
|-----------|--------------------------------------------------------------------------------|
| `<expr>`  | An expression of string type (e.g. VARCHAR) that holds valid JSON information. |

## Return Type

VARIANT

## SQL Examples

```sql
SELECT parse_json('[-1, 12, 289, 2188, false]');
┌──────────────────────────────────────────┐
│ parse_json('[-1, 12, 289, 2188, false]') │
├──────────────────────────────────────────┤
│ [-1,12,289,2188,false]                   │
└──────────────────────────────────────────┘

SELECT try_parse_json('{ "x" : "abc", "y" : false, "z": 10} ');
┌─────────────────────────────────────────────────────────┐
│ try_parse_json('{ "x" : "abc", "y" : false, "z": 10} ') │
├─────────────────────────────────────────────────────────┤
│ {"x":"abc","y":false,"z":10}                            │
└─────────────────────────────────────────────────────────┘
```
