---
title: ST_POINT (Lakehouse v2)
description: ST_POINT — crée une géométrie de type point à partir de valeurs de longitude et de latitude.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/17-spatial-functions/st-point.md
---

Crée une géométrie de type point à partir de valeurs de longitude et de latitude.

## Syntaxe Analyze

```python
func.st_point(<lng>, <lat>)
```

## Exemples Analyze

```python
func.st_point(-73.9857, 40.7484)

┌────────────┐
│ (geometry)  │
└────────────┘
```

## Syntaxe SQL

```sql
ST_POINT(<lng>, <lat>)
```

## Exemples SQL

```sql
SELECT ST_ASTEXT(ST_POINT(-73.9857, 40.7484));

┌──────────────────────────┐
│ POINT (-73.9857 40.7484)  │
└──────────────────────────┘
```
