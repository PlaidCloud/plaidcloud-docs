---
title: PI
description: "Learn how to use the PI numeric function in PlaidCloud Lakehouse. Returns the value of π as a floating-point value. Includes syntax and examples."
---

Returns the value of π as a floating-point value.

## Analyze Syntax

```python
func.pi()
```

## Analyze Examples

```python
func.pi()

┌───────────────────┐
│     func.pi()     │
├───────────────────┤
│ 3.141592653589793 │
└───────────────────┘
```

## SQL Syntax

```sql
PI()
```

## SQL Examples

```sql
SELECT PI();

┌───────────────────┐
│        pi()       │
├───────────────────┤
│ 3.141592653589793 │
└───────────────────┘
```