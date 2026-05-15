---
title: ST_CIRCLE (Lakehouse v2)
description: ST_CIRCLE — creates a circle geometry from a center longitude, latitude and radius in meters.
---

Creates a circle geometry from a center longitude, latitude and radius in meters.

## Analyze Syntax

```python
func.st_circle(<lng>, <lat>, <radius>)
```

## Analyze Examples

```python
func.st_circle(0, 0, 100)

┌────────────┐
│ (geometry)  │
└────────────┘
```

## SQL Syntax

```sql
ST_CIRCLE(<lng>, <lat>, <radius>)
```

## SQL Examples

```sql
SELECT ST_ASTEXT(ST_CIRCLE(0, 0, 100));

┌─────────────────────┐
│ CIRCLE((0, 0), 100)  │
└─────────────────────┘
```
