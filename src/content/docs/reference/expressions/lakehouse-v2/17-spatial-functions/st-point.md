---
title: ST_POINT (Lakehouse v2)
description: ST_POINT — Creates a point geometry from longitude and latitude values.
---

Creates a point geometry from longitude and latitude values.

## Analyze Syntax

```python
func.st_point(<lng>, <lat>)
```

## Analyze Examples

```python
func.st_point(-73.9857, 40.7484)

┌────────────┐
│ (geometry)  │
└────────────┘
```

## SQL Syntax

```sql
ST_POINT(<lng>, <lat>)
```

## SQL Examples

```sql
SELECT ST_ASTEXT(ST_POINT(-73.9857, 40.7484));

┌──────────────────────────┐
│ POINT (-73.9857 40.7484)  │
└──────────────────────────┘
```
