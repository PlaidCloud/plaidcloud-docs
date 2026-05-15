---
title: ST_Y (Lakehouse v2)
description: ST_Y — Returns the Y coordinate (latitude) of a point geometry.
---

Returns the Y coordinate (latitude) of a point geometry.

## Analyze Syntax

```python
func.st_y(<point>)
```

## Analyze Examples

```python
func.st_y(func.st_point(1.5, 2.5))

┌─────┐
│ 2.5  │
└─────┘
```

## SQL Syntax

```sql
ST_Y(<point>)
```

## SQL Examples

```sql
SELECT ST_Y(ST_POINT(1.5, 2.5));

┌─────┐
│ 2.5  │
└─────┘
```
