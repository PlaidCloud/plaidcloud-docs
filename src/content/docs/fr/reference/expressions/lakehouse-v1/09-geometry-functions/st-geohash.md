---
title: ST_GEOHASH (Lakehouse v1)
description: ST_GEOHASH — renvoie le geohash d'un objet GEOMETRY.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-geohash.md
---

Renvoie le [geohash](https://en.wikipedia.org/wiki/Geohash) d'un objet GEOMETRY. Un geohash est une courte chaîne en base32 qui identifie un rectangle géodésique contenant un lieu dans le monde. L'argument facultatif de précision définit la `precision` du geohash renvoyé. Par exemple, passer 5 pour `precision renvoie un geohash plus court (5 caractères) et moins précis.

## Syntaxe SQL

```sql
ST_GEOHASH(<geometry> [, <precision>])
```

## Arguments

| Arguments       | Description                                                               |
|-----------------|---------------------------------------------------------------------------|
| `geometry`    | L'argument doit être une expression de type GEOMETRY.                      |
| `[precision]` | Facultatif. Définit la précision du geohash renvoyé ; la valeur par défaut est 12. |

## Type de retour

String.

## Exemples SQL

```sql
SELECT
  ST_GEOHASH(
    ST_GEOMETRYFROMWKT(
      'POINT(-122.306100 37.554162)'
    )
  ) AS pipeline_geohash;

┌──────────────────┐
│ pipeline_geohash │
├──────────────────┤
│ 9q9j8ue2v71y     │
└──────────────────┘

SELECT
  ST_GEOHASH(
    ST_GEOMETRYFROMWKT(
      'SRID=4326;POINT(-122.35 37.55)'
    ),
    5
  ) AS pipeline_geohash;

┌──────────────────┐
│ pipeline_geohash │
├──────────────────┤
│ 9q8vx            │
└──────────────────┘
```
