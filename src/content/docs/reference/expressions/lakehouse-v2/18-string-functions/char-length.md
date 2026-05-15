---
title: CHAR_LENGTH (Lakehouse v2)
description: CHAR_LENGTH — returns the number of characters in a string.
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
