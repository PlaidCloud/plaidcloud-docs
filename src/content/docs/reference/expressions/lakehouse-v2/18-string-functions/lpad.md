---
title: LPAD (Lakehouse v2)
description: LPAD — pads a string on the left to a specified length with a fill string.
---

Pads a string on the left to a specified length with a fill string.

## Analyze Syntax

```python
func.lpad(<str>, <len>, <pad>)
```

## Analyze Examples

```python
func.lpad('42', 5, '0')

┌─────────┐
│ '00042'  │
└─────────┘
```

## SQL Syntax

```sql
LPAD(<str>, <len>, <pad>)
```

## SQL Examples

```sql
SELECT LPAD('42', 5, '0');

┌───────┐
│ 00042  │
└───────┘
```
