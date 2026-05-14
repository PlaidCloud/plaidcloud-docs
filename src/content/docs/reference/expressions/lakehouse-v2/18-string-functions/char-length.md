---
title: CHAR_LENGTH
description: "Learn how to use the CHAR_LENGTH string function in PlaidCloud Lakehouse. Returns the number of characters in a string - see syntax, examples, and output."
---

Returns the number of characters in a string.

## Analyze Syntax

```python
func.char_length(<str>)
```

## Analyze Examples

```python
func.char_length('hello world')

┌────┐
│ 11  │
└────┘
```

## SQL Syntax

```sql
CHAR_LENGTH(<str>)
```

## SQL Examples

```sql
SELECT CHAR_LENGTH('hello world');

┌────┐
│ 11  │
└────┘
```
