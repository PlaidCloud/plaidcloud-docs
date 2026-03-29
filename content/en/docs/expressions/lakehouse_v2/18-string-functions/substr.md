---
title: SUBSTR
---

Returns a substring starting from a specified position with an optional length.

## Analyze Syntax

```python
func.substr(<str>, <pos>[, <len>])
```

## Analyze Examples

```python
func.substr('StarRocks', 5, 5)

┌─────────┐
│ 'Rocks'  │
└─────────┘
```

## SQL Syntax

```sql
SUBSTR(<str>, <pos>[, <len>])
```

## SQL Examples

```sql
SELECT SUBSTR('StarRocks', 5, 5);

┌───────┐
│ Rocks  │
└───────┘
```
