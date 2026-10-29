---
title: ST_TRANSFORM (Lakehouse v1)
description: ST_TRANSFORM — wandelt ein GEOMETRY-Objekt von einem räumlichen Bezugssystem (SRS) in ein anderes um.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-transform.md
---

Wandelt ein GEOMETRY-Objekt von einem [räumlichen Bezugssystem (SRS)](https://en.wikipedia.org/wiki/Spatial_reference_system) in ein anderes um. Wenn Sie nur die SRID ändern müssen, ohne die Koordinaten zu ändern (z. B. weil die SRID falsch war), verwenden Sie stattdessen [ST_SETSRID](../st-setsrid).

## SQL-Syntax

```sql
ST_TRANSFORM(<geometry> [, <from_srid>], <to_srid>)
```

## Argumente

| Argumente     | Beschreibung                                                                                                                                                              |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `<geometry>`  | Das Argument muss ein Ausdruck vom Typ GEOMETRY-Objekt sein.                                                                                                              |
| `<from_srid>` | Optionale SRID, die das aktuelle SRS des eingegebenen GEOMETRY-Objekts angibt. Wird dieses Argument weggelassen, wird die im eingegebenen GEOMETRY-Objekt angegebene SRID verwendet. |
| `<to_srid>`   | Die SRID, die das zu verwendende SRS angibt; das eingegebene GEOMETRY-Objekt wird in ein neues Objekt umgewandelt, das dieses SRS verwendet.                              |

## Rückgabetyp

Geometry.

## SQL-Beispiele

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
