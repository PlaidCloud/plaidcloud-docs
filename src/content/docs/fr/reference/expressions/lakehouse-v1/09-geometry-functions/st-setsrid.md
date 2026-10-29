---
title: ST_SETSRID (Lakehouse v1)
description: ST_SETSRID — renvoie un objet GEOMETRY dont le SRID (identifiant du système de référence spatiale) est défini sur la valeur indiquée.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-setsrid.md
---

Renvoie un objet GEOMETRY dont le [SRID (identifiant du système de référence spatiale)](https://en.wikipedia.org/wiki/Spatial_reference_system#Identifier) est défini sur la valeur indiquée. Cette fonction ne modifie que le SRID, sans toucher aux coordonnées de l'objet. Si vous devez aussi modifier les coordonnées pour qu'elles correspondent au nouveau SRS (système de référence spatiale), utilisez plutôt [ST_TRANSFORM](../st-transform).

## Syntaxe SQL

```sql
ST_SETSRID(<geometry>, <srid>)
```

## Arguments

| Arguments    | Description                                                 |
|--------------|-------------------------------------------------------------|
| `<geometry>` | L'argument doit être une expression de type objet GEOMETRY. |
| `<srid>`     | L'entier SRID à définir dans l'objet GEOMETRY renvoyé.      |

## Type de retour

Geometry.

## Exemples SQL

```sql
SET GEOMETRY_OUTPUT_FORMAT = 'EWKT'

SELECT ST_SETSRID(TO_GEOMETRY('POINT(13 51)'), 4326) AS geometry

┌────────────────────────┐
│        geometry        │
├────────────────────────┤
│ SRID=4326;POINT(13 51) │
└────────────────────────┘

```
