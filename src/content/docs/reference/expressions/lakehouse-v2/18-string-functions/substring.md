---
title: SUBSTRING (Lakehouse v2)
description: SUBSTRING — returns a substring starting from a specified position. Alias for `SUBSTR`.
---

Returns a substring starting from a specified position. Alias for `SUBSTR`.

## Analyze Syntax

```python
func.substring(<str>, <pos>[, <len>])
```

## Analyze Examples

```python
func.substring('StarRocks', 1, 4)

┌────────┐
│ 'Star'  │
└────────┘
```

## SQL Syntax

```sql
SUBSTRING(<str>, <pos>[, <len>])
```

## SQL Examples

```sql
SELECT SUBSTRING('StarRocks', 1, 4);

┌──────┐
│ Star  │
└──────┘
```
