---
title: UNNEST
description: "Learn how to use the UNNEST array function in PlaidCloud Lakehouse. Expands an array into a set of rows - see syntax, examples, and output."
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
