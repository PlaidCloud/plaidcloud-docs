---
title: ARRAY_APPEND
description: "Learn how to use the ARRAY_APPEND array function in PlaidCloud Lakehouse. Prepends an element to the array. Full syntax and usage reference."
---

Prepends an element to the array.

## Analyze Syntax

```python
func.array_append( <array>, <element>)
```

## Analyze Examples

```python
func.array_append([3, 4], 5)

┌──────────────────────────────┐
│ func.array_append([3, 4], 5) │
├──────────────────────────────┤
│ [3,4,5]                      │
└──────────────────────────────┘
```

## SQL Syntax

```sql
ARRAY_APPEND( <array>, <element>)
```

## SQL Examples

```sql
SELECT ARRAY_APPEND([3, 4], 5);

┌─────────────────────────┐
│ array_append([3, 4], 5) │
├─────────────────────────┤
│ [3,4,5]                 │
└─────────────────────────┘
```