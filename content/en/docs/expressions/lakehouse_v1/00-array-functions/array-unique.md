---
title: ARRAY_UNIQUE
description: "Learn how to use the ARRAY_UNIQUE array function in PlaidCloud Lakehouse. Counts unique elements in the array (except NULL). Includes syntax and examples."
---

Counts unique elements in the array (except NULL).

## Analyze Syntax

```python
func.array_unique( <array> )
```

## Analyze Examples

```python
func.array_unique([1, 2, 3, 3, 4])

┌─────────────────────────────────────┐
│ func.array_unique([1, 2, 3, 3, 4])  │
├─────────────────────────────────────┤
│                                   4 │
└─────────────────────────────────────┘
```

## SQL Syntax

```sql
ARRAY_UNIQUE( <array> )
```

## SQL Examples

```sql
SELECT ARRAY_UNIQUE([1, 2, 3, 3, 4]);

┌───────────────────────────────┐
│ array_unique([1, 2, 3, 3, 4]) │
├───────────────────────────────┤
│                             4 │
└───────────────────────────────┘
```