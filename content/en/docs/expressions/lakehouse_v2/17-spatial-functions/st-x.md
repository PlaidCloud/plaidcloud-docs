---
title: ST_X
description: "Learn how to use the ST_X spatial function in PlaidCloud Lakehouse. Returns the X coordinate (longitude) of a point geometry - with syntax and examples."
---

Returns the X coordinate (longitude) of a point geometry.

## Analyze Syntax

```python
func.st_x(<point>)
```

## Analyze Examples

```python
func.st_x(func.st_point(1.5, 2.5))

┌─────┐
│ 1.5  │
└─────┘
```

## SQL Syntax

```sql
ST_X(<point>)
```

## SQL Examples

```sql
SELECT ST_X(ST_POINT(1.5, 2.5));

┌─────┐
│ 1.5  │
└─────┘
```
