---
title: UNNEST (Lakehouse v2)
description: UNNEST — expands an array into a set of rows.
---

Expands an array into a set of rows.

## Analyze Syntax

```python
func.unnest([1, 2, 3])
```

## Analyze Examples

```python
# Used in FROM clause
# SELECT * FROM UNNEST([1, 2, 3])
```

## SQL Syntax

```sql
UNNEST([1, 2, 3])
```

## SQL Examples

```sql
SELECT * FROM UNNEST([1, 2, 3]) AS t(val);

┌─────┐
│ val │
├─────┤
│   1 │
│   2 │
│   3 │
└─────┘
```
