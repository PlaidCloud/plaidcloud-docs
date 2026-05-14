---
title: ARRAY_LENGTH
description: "Learn how to use the ARRAY_LENGTH array function in PlaidCloud Lakehouse. Returns the length of an array. Includes usage and syntax details."
---

Returns the length of an array.

## Analyze Syntax

```python
func.array_length( <array> )
```

## Analyze Examples

```python
func.array_length([1, 2])

┌────────────────────────────┐
│ func.array_length([1, 2])  │
├────────────────────────────┤
│                          2 │
└────────────────────────────┘
```

## SQL Syntax

```sql
ARRAY_LENGTH( <array> )
```

## SQL Examples

```sql
SELECT ARRAY_LENGTH([1, 2]);

┌──────────────────────┐
│ array_length([1, 2]) │
├──────────────────────┤
│                    2 │
└──────────────────────┘
```
