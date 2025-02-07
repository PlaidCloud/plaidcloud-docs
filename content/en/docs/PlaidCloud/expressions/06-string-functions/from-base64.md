---
title: FROM_BASE64
---

Takes a string encoded with the base-64 encoded rules nd returns the decoded result as a binary.
The result is NULL if the argument is NULL or not a valid base-64 string.

# Analyze Syntax

```python
func.from_base64(<expr>)
```

## Analyze Examples
```python
func.from_base64('YWJj')
+--------------------------+
| func.from_base64('YWJj') |
+--------------------------+
| abc                      |
+--------------------------+
```

## SQL Syntax

```sql
FROM_BASE64(<expr>)
```

## Arguments

| Arguments | Description       |
|-----------|-------------------|
| `<expr>`  | The string value. |

## Return Type

`BINARY`

## SQL Examples

```sql
SELECT TO_BASE64('abc'), FROM_BASE64(TO_BASE64('abc')) as b, b::String;
┌───────────────────────────────────────┐
│ to_base64('abc') │    b   │ b::string │
│      String      │ Binary │   String  │
├──────────────────┼────────┼───────────┤
│ YWJj             │ 616263 │ abc       │
└───────────────────────────────────────┘
```
