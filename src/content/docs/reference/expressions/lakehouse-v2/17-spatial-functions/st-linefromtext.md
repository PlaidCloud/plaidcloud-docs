---
title: ST_LINEFROMTEXT
description: ST_LINEFROMTEXT — creates a line geometry from a WKT string - see syntax, examples, and output.
---

Creates a line geometry from a WKT string.

## Analyze Syntax

```python
func.st_linefromtext(<wkt>)
```

## Analyze Examples

```python
func.st_linefromtext('LINESTRING (0 0, 1 1, 2 2)')

┌────────────┐
│ (geometry)  │
└────────────┘
```

## SQL Syntax

```sql
ST_LINEFROMTEXT(<wkt>)
```

## SQL Examples

```sql
SELECT ST_ASTEXT(ST_LINEFROMTEXT('LINESTRING (0 0, 1 1, 2 2)'));

┌────────────────────────────┐
│ LINESTRING (0 0, 1 1, 2 2)  │
└────────────────────────────┘
```
