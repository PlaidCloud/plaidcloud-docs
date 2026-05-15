---
title: ARRAYS_ZIP
description: ARRAYS_ZIP — merges multiple arrays into an array of structs - see syntax, examples, and output.
---

Merges multiple arrays into an array of structs.

## Analyze Syntax

```python
func.arrays_zip([1,2], ['a','b'])
```

## Analyze Examples

```python
func.arrays_zip([1, 2, 3], ['a', 'b', 'c'])

┌───────────────────────────┐
│ [{1,'a'},{2,'b'},{3,'c'}] │
└───────────────────────────┘
```

## SQL Syntax

```sql
ARRAYS_ZIP([1,2], ['a','b'])
```

## SQL Examples

```sql
SELECT ARRAYS_ZIP([1, 2, 3], ['a', 'b', 'c']);

┌───────────────────────────────────────────────────┐
│ [{"0":1,"1":"a"},{"0":2,"1":"b"},{"0":3,"1":"c"}] │
└───────────────────────────────────────────────────┘
```
