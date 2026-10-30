---
title: ST_X (Lakehouse v2)
description: ST_X — Gibt die X-Koordinate (Längengrad) einer Punktgeometrie zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/17-spatial-functions/st-x.md
---

Gibt die X-Koordinate (Längengrad) einer Punktgeometrie zurück.

## Analyze-Syntax

```python
func.st_x(<point>)
```

## Analyze-Beispiele

```python
func.st_x(func.st_point(1.5, 2.5))

┌─────┐
│ 1.5  │
└─────┘
```

## SQL-Syntax

```sql
ST_X(<point>)
```

## SQL-Beispiele

```sql
SELECT ST_X(ST_POINT(1.5, 2.5));

┌─────┐
│ 1.5  │
└─────┘
```
