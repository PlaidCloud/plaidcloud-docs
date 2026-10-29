---
title: ST_SETSRID (Lakehouse v1)
description: ST_SETSRID — gibt ein GEOMETRY-Objekt zurück, dessen SRID (Spatial Reference System Identifier) auf den angegebenen Wert gesetzt ist.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-setsrid.md
---

Gibt ein GEOMETRY-Objekt zurück, dessen [SRID (Spatial Reference System Identifier)](https://en.wikipedia.org/wiki/Spatial_reference_system#Identifier) auf den angegebenen Wert gesetzt ist. Diese Funktion ändert nur die SRID, ohne die Koordinaten des Objekts zu beeinflussen. Wenn Sie zusätzlich die Koordinaten an das neue SRS (Spatial Reference System) anpassen müssen, verwenden Sie stattdessen [ST_TRANSFORM](../st-transform).

## SQL-Syntax

```sql
ST_SETSRID(<geometry>, <srid>)
```

## Argumente

| Argumente    | Beschreibung                                                          |
|--------------|-----------------------------------------------------------------------|
| `<geometry>` | Das Argument muss ein Ausdruck vom Typ GEOMETRY-Objekt sein.          |
| `<srid>`     | Die SRID als Ganzzahl, die im zurückgegebenen GEOMETRY-Objekt gesetzt wird. |

## Rückgabetyp

Geometry.

## SQL-Beispiele

```sql
SET GEOMETRY_OUTPUT_FORMAT = 'EWKT'

SELECT ST_SETSRID(TO_GEOMETRY('POINT(13 51)'), 4326) AS geometry

┌────────────────────────┐
│        geometry        │
├────────────────────────┤
│ SRID=4326;POINT(13 51) │
└────────────────────────┘

```
