---
title: LOCATE
---

Returns the position of the first occurrence of a substring in a string.

## Analyze Syntax

```python
func.locate(<substr>, <str>[, <pos>])
```

## Analyze Examples

```python
func.locate('or', 'hello world')

┌───┐
│ 8  │
└───┘
```

## SQL Syntax

```sql
LOCATE(<substr>, <str>[, <pos>])
```

## SQL Examples

```sql
SELECT LOCATE('or', 'hello world');

┌───┐
│ 8  │
└───┘
```
