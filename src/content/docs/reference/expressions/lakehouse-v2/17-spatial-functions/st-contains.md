---
title: ST_CONTAINS (Lakehouse v2)
description: ST_CONTAINS — checks whether one geometry contains another. Returns 1 if true.
---

Checks whether one geometry contains another. Returns 1 if true.

## Analyze Syntax

```python
func.st_contains(<geometry1>, <geometry2>)
```

## Analyze Examples

```python
func.st_contains(get_column(table, 'area'), func.st_point(1, 1))

┌───┐
│ 1  │
└───┘
```

## SQL Syntax

```sql
ST_CONTAINS(<geometry1>, <geometry2>)
```

## SQL Examples

```sql
SELECT ST_CONTAINS(ST_GeomFromText('POLYGON((0 0,10 0,10 10,0 10,0 0))'), ST_POINT(5, 5));

┌───┐
│ 1  │
└───┘
```
