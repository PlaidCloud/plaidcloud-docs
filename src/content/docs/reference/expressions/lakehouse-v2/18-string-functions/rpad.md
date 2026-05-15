---
title: RPAD (Lakehouse v2)
description: RPAD — pads a string on the right to a specified length with a fill string.
---

Pads a string on the right to a specified length with a fill string.

## Analyze Syntax

```python
func.rpad(<str>, <len>, <pad>)
```

## Analyze Examples

```python
func.rpad('hello', 10, '.')

┌──────────────┐
│ 'hello.....'  │
└──────────────┘
```

## SQL Syntax

```sql
RPAD(<str>, <len>, <pad>)
```

## SQL Examples

```sql
SELECT RPAD('hello', 10, '.');

┌────────────┐
│ hello.....  │
└────────────┘
```
