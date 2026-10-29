---
title: ST_CIRCLE (Lakehouse v2)
description: ST_CIRCLE — crée une géométrie de cercle à partir de la longitude et de la latitude du centre et d'un rayon en mètres.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/17-spatial-functions/st-circle.md
---

Crée une géométrie de cercle à partir de la longitude et de la latitude du centre et d'un rayon en mètres.

## Syntaxe Analyze

```python
func.st_circle(<lng>, <lat>, <radius>)
```

## Exemples Analyze

```python
func.st_circle(0, 0, 100)

┌────────────┐
│ (geometry)  │
└────────────┘
```

## Syntaxe SQL

```sql
ST_CIRCLE(<lng>, <lat>, <radius>)
```

## Exemples SQL

```sql
SELECT ST_ASTEXT(ST_CIRCLE(0, 0, 100));

┌─────────────────────┐
│ CIRCLE((0, 0), 100)  │
└─────────────────────┘
```
