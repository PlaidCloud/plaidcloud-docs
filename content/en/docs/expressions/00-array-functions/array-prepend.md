---
title: ARRAY_PREPEND
---

Prepends an element to the array.

## Analyze Syntax

```python
func.array_prepend( <element>, <array> )
```

## Analyze Examples

```python
func.array_prepend(1, [3, 4])

┌────────────────────────────────┐
│ func.array_prepend(1, [3, 4])  │
├────────────────────────────────┤
│ [1,3,4]                        │
└────────────────────────────────┘
```

## SQL Syntax

```sql
ARRAY_PREPEND( <element>, <array> )
```

## SQL Examples

```sql
SELECT ARRAY_PREPEND(1, [3, 4]);

┌──────────────────────────┐
│ array_prepend(1, [3, 4]) │
├──────────────────────────┤
│ [1,3,4]                  │
└──────────────────────────┘
```