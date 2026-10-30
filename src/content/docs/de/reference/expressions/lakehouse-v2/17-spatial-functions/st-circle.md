---
title: ST_CIRCLE (Lakehouse v2)
description: ST_CIRCLE – erstellt eine Kreisgeometrie aus dem Längengrad und Breitengrad des Mittelpunkts sowie einem Radius in Metern.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/17-spatial-functions/st-circle.md
---

Erstellt eine Kreisgeometrie aus dem Längengrad und Breitengrad des Mittelpunkts sowie einem Radius in Metern.

## Analyze-Syntax

```python
func.st_circle(<lng>, <lat>, <radius>)
```

## Analyze-Beispiele

```python
func.st_circle(0, 0, 100)

┌────────────┐
│ (geometry)  │
└────────────┘
```

## SQL-Syntax

```sql
ST_CIRCLE(<lng>, <lat>, <radius>)
```

## SQL-Beispiele

```sql
SELECT ST_ASTEXT(ST_CIRCLE(0, 0, 100));

┌─────────────────────┐
│ CIRCLE((0, 0), 100)  │
└─────────────────────┘
```
