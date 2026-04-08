---
title: ARRAY_PREPEND
description: "Learn how to use the ARRAY_PREPEND array function in PlaidCloud Lakehouse. Prepends an element to the array. Full syntax and usage reference."
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