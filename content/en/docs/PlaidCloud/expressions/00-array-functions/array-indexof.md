---
title: ARRAY_INDEXOF
---

Returns the index(1-based) of an element if the array contains the element.

## Analyze Syntax

```python
func.array_indexof( <array>, <element> )
```

## Analyze Examples

```python
func.array_indexof([1, 2, 9], 9)

┌───────────────────────────────────┐
│ func.array_indexof([1, 2, 9], 9)  │
├───────────────────────────────────┤
│                                 3 │
└───────────────────────────────────┘
```

## SQL Syntax

```sql
ARRAY_INDEXOF( <array>, <element> )
```

## SQL Examples

```sql
SELECT ARRAY_INDEXOF([1, 2, 9], 9);

┌─────────────────────────────┐
│ array_indexof([1, 2, 9], 9) │
├─────────────────────────────┤
│                           3 │
└─────────────────────────────┘
```