---
title: REPEAT (Lakehouse v2)
description: REPEAT — repeats a string a specified number of times.
---

Repeats a string a specified number of times.

## Analyze Syntax

```python
func.repeat(<str>, <n>)
```

## Analyze Examples

```python
func.repeat('ab', 3)

┌──────────┐
│ 'ababab'  │
└──────────┘
```

## SQL Syntax

```sql
REPEAT(<str>, <n>)
```

## SQL Examples

```sql
SELECT REPEAT('ab', 3);

┌────────┐
│ ababab  │
└────────┘
```
