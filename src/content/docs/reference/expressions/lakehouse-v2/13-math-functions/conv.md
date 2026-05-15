---
title: CONV
description: CONV — converts a number from one base to another - see syntax, examples, and output.
---

Converts a number from one base to another.

## Analyze Syntax

```python
func.conv(<num>, <from_base>, <to_base>)
```

## Analyze Examples

```python
func.conv('ff', 16, 10)

┌───────┐
│ '255'  │
└───────┘
```

## SQL Syntax

```sql
CONV(<num>, <from_base>, <to_base>)
```

## SQL Examples

```sql
SELECT CONV('ff', 16, 10);

┌─────┐
│ 255  │
└─────┘
```
