---
title: ARRAY_LENGTH
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