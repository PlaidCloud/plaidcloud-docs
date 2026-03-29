---
title: INSTR
---

Returns the position of the first occurrence of a substring in a string.

## Analyze Syntax

```python
func.instr(<str>, <substr>)
```

## Analyze Examples

```python
func.instr('hello world', 'world')

┌───┐
│ 7  │
└───┘
```

## SQL Syntax

```sql
INSTR(<str>, <substr>)
```

## SQL Examples

```sql
SELECT INSTR('hello world', 'world');

┌───┐
│ 7  │
└───┘
```
