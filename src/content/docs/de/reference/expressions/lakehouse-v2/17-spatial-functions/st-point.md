---
title: ST_POINT (Lakehouse v2)
description: ST_POINT — Erstellt eine Punktgeometrie aus Längen- und Breitengradwerten.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/17-spatial-functions/st-point.md
---

Erstellt eine Punktgeometrie aus Längen- und Breitengradwerten.

## Analyze-Syntax

```python
func.st_point(<lng>, <lat>)
```

## Analyze-Beispiele

```python
func.st_point(-73.9857, 40.7484)

┌────────────┐
│ (geometry)  │
└────────────┘
```

## SQL-Syntax

```sql
ST_POINT(<lng>, <lat>)
```

## SQL-Beispiele

```sql
SELECT ST_ASTEXT(ST_POINT(-73.9857, 40.7484));

┌──────────────────────────┐
│ POINT (-73.9857 40.7484)  │
└──────────────────────────┘
```
