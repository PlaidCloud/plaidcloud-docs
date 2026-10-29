---
title: ST_TRANSFORM (Lakehouse v1)
description: ST_TRANSFORM — convertit un objet GEOMETRY d'un système de référence spatiale (SRS) vers un autre.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-transform.md
---

Convertit un objet GEOMETRY d'un [système de référence spatiale (SRS)](https://en.wikipedia.org/wiki/Spatial_reference_system) vers un autre. Si vous devez seulement modifier le SRID sans changer les coordonnées (par exemple, si le SRID était incorrect), utilisez plutôt [ST_SETSRID](../st-setsrid).

## Syntaxe SQL

```sql
ST_TRANSFORM(<geometry> [, <from_srid>], <to_srid>)
```

## Arguments

| Arguments     | Description                                                                                                                                               |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| `<geometry>`  | L'argument doit être une expression de type objet GEOMETRY.                                                                                               |
| `<from_srid>` | SRID facultatif qui identifie le SRS actuel de l'objet GEOMETRY en entrée ; s'il est omis, le SRID spécifié dans l'objet GEOMETRY en entrée est utilisé. |
| `<to_srid>`   | Le SRID qui identifie le SRS à utiliser ; l'objet GEOMETRY en entrée est transformé en un nouvel objet qui utilise ce SRS.                                |

## Type de retour

Geometry.

## Exemples SQL

```sql
SET GEOMETRY_OUTPUT_FORMAT = 'EWKT'

SELECT ST_TRANSFORM(ST_GEOMFROMWKT('POINT(389866.35 5819003.03)', 32633), 3857) AS transformed_geom

┌───────────────────────────────────────────────┐
│                transformed_geom               │
├───────────────────────────────────────────────┤
│ SRID=3857;POINT(1489140.093766 6892872.19868) │
└───────────────────────────────────────────────┘

SELECT ST_TRANSFORM(ST_GEOMFROMWKT('POINT(4.500212 52.161170)'), 4326, 28992) AS transformed_geom

┌──────────────────────────────────────────────┐
│               transformed_geom               │
├──────────────────────────────────────────────┤
│ SRID=28992;POINT(94308.670475 464038.168827) │
└──────────────────────────────────────────────┘

```
