---
title: ST_NPOINTS (Lakehouse v1)
description: ST_NPOINTS — gibt die Anzahl der Punkte in einem GEOMETRY-Objekt zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-npoints.md
---

Gibt die Anzahl der Punkte in einem GEOMETRY-Objekt zurück.

## SQL-Syntax

```sql
ST_NPOINTS(<geometry>)
```

## Aliase

- [ST_NUMPOINTS](../st-numpoints)

## Argumente

| Argumente    | Beschreibung                                                   |
|--------------|----------------------------------------------------------------|
| `<geometry>` | Das Argument muss ein Ausdruck vom Typ GEOMETRY-Objekt sein.   |

## Rückgabetyp

UInt8.

## SQL-Beispiele

```sql
SELECT ST_NPOINTS(TO_GEOMETRY('POINT(66 12)')) AS npoints

┌─────────┐
│ npoints │
├─────────┤
│       1 │
└─────────┘

SELECT ST_NPOINTS(TO_GEOMETRY('MULTIPOINT((45 21),(12 54))')) AS npoints

┌─────────┐
│ npoints │
├─────────┤
│       2 │
└─────────┘

SELECT ST_NPOINTS(TO_GEOMETRY('LINESTRING(40 60,50 50,60 40)')) AS npoints

┌─────────┐
│ npoints │
├─────────┤
│       3 │
└─────────┘

SELECT ST_NPOINTS(TO_GEOMETRY('MULTILINESTRING((1 1,32 17),(33 12,73 49,87.1 6.1))')) AS npoints

┌─────────┐
│ npoints │
├─────────┤
│       5 │
└─────────┘

SELECT ST_NPOINTS(TO_GEOMETRY('GEOMETRYCOLLECTION(POLYGON((-10 0,0 10,10 0,-10 0)),LINESTRING(40 60,50 50,60 40),POINT(99 11))')) AS npoints

┌─────────┐
│ npoints │
├─────────┤
│       8 │
└─────────┘
```
