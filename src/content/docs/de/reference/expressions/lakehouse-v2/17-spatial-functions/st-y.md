---
title: ST_Y (Lakehouse v2)
description: ST_Y — Gibt die Y-Koordinate (Breitengrad) einer Punktgeometrie zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/17-spatial-functions/st-y.md
---

Gibt die Y-Koordinate (Breitengrad) einer Punktgeometrie zurück.

## Analyze-Syntax

```python
func.st_y(<point>)
```

## Analyze-Beispiele

```python
func.st_y(func.st_point(1.5, 2.5))

┌─────┐
│ 2.5  │
└─────┘
```

## SQL-Syntax

```sql
ST_Y(<point>)
```

## SQL-Beispiele

```sql
SELECT ST_Y(ST_POINT(1.5, 2.5));

┌─────┐
│ 2.5  │
└─────┘
```
