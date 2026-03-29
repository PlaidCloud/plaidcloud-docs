---
title: RANGE
---

Returns an array collected by [start, end).

## Analyze Syntax

```python
func.range( <start>, <end> )
```

## SQAnalyzeL Examples

```python
func.range(1, 5)

┌────────────────────┐
│  func.range(1, 5)  │
├────────────────────┤
│ [1,2,3,4]          │
└────────────────────┘
```

## SQL Syntax

```sql
RANGE( <start>, <end> )
```

## SQL Examples

```sql
SELECT RANGE(1, 5);

┌───────────────┐
│  range(1, 5)  │
├───────────────┤
│ [1,2,3,4]     │
└───────────────┘
```