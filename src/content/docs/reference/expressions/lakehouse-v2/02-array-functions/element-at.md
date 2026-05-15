---
title: ELEMENT_AT
description: ELEMENT_AT — returns the element at a specified position in an array (1-indexed).
---

Returns the element at a specified position in an array (1-indexed).

## Analyze Syntax

```python
func.element_at([10, 20, 30], 2)
```

## Analyze Examples

```python
func.element_at([10, 20, 30], 2)

┌────┐
│ 20 │
└────┘
```

## SQL Syntax

```sql
ELEMENT_AT([10, 20, 30], 2)
```

## SQL Examples

```sql
SELECT ELEMENT_AT([10, 20, 30], 2);

┌────┐
│ 20 │
└────┘
```
