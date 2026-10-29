---
title: ST_ASWKB (Lakehouse v1)
description: ST_ASWKB — wandelt ein GEOMETRY-Objekt in eine Darstellung im Format WKB (Well-Known Binary) um.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-aswkb.md
---

Wandelt ein GEOMETRY-Objekt in eine Darstellung im Format [WKB (Well-Known Binary)](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry#Well-known_binary) um.

## SQL-Syntax

```sql
ST_ASWKB(<geometry>)
```

## Aliase

- [ST_ASBINARY](../st-asbinary)

## Argumente

| Argumente    | Beschreibung                                          |
|--------------|-------------------------------------------------------|
| `<geometry>` | Das Argument muss ein Ausdruck vom Typ GEOMETRY sein. |

## Rückgabetyp

Binary.

## SQL-Beispiele

```sql
SELECT
  ST_ASWKB(
    ST_GEOMETRYFROMWKT(
      'SRID=4326;LINESTRING(400000 6000000, 401000 6010000)'
    )
  ) AS pipeline_wkb;

┌────────────────────────────────────────────────────────────────────────────────────┐
│                                    pipeline_wkb                                    │
├────────────────────────────────────────────────────────────────────────────────────┤
│ 01020000000200000000000000006A18410000000060E3564100000000A07918410000000024ED5641 │
└────────────────────────────────────────────────────────────────────────────────────┘

SELECT
  ST_ASBINARY(
    ST_GEOMETRYFROMWKT(
      'SRID=4326;POINT(-122.35 37.55)'
    )
  ) AS pipeline_wkb;

┌────────────────────────────────────────────┐
│                pipeline_wkb                │
├────────────────────────────────────────────┤
│ 01010000006666666666965EC06666666666C64240 │
└────────────────────────────────────────────┘
```
