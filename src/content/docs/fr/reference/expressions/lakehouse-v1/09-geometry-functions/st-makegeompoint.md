---
title: ST_MAKEGEOMPOINT (Lakehouse v1)
description: ST_MAKEGEOMPOINT — construit un objet GEOMETRY qui représente un Point avec la longitude et la latitude indiquées.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-makegeompoint.md
---

Construit un objet GEOMETRY qui représente un Point avec la longitude et la latitude indiquées.

## Syntaxe SQL

```sql
ST_MAKEGEOMPOINT(<longitude>, <latitude>)
```

## Alias

- [ST_GEOM_POINT](../st-geom-point)

## Arguments

| Arguments     | Description                                   |
|---------------|-----------------------------------------------|
| `<longitude>` | Une valeur Double qui représente la longitude. |
| `<latitude>`  | Une valeur Double qui représente la latitude.  |

## Type de retour

Geometry.

## Exemples SQL

```sql
SELECT
  ST_MAKEGEOMPOINT(
    7.0, 8.0
  ) AS pipeline_point;

┌────────────────┐
│ pipeline_point │
├────────────────┤
│ POINT(7 8)     │
└────────────────┘

SELECT
  ST_MAKEGEOMPOINT(
    -122.3061, 37.554162
  ) AS pipeline_point;

┌────────────────────────────┐
│       pipeline_point       │
├────────────────────────────┤
│ POINT(-122.3061 37.554162) │
└────────────────────────────┘
```
