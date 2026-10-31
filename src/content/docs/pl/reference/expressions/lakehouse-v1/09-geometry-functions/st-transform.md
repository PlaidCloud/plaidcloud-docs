---
title: ST_TRANSFORM (Lakehouse v1)
description: ST_TRANSFORM — konwertuje obiekt GEOMETRY z jednego układu odniesienia przestrzennego (SRS) do innego.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-transform.md
---

Konwertuje obiekt GEOMETRY z jednego [układu odniesienia przestrzennego (SRS)](https://en.wikipedia.org/wiki/Spatial_reference_system) do innego. Jeśli wystarczy zmienić SRID bez zmiany współrzędnych (np. gdy SRID był nieprawidłowy), użyj zamiast tego funkcji [ST_SETSRID](../st-setsrid).

## Składnia SQL

```sql
ST_TRANSFORM(<geometry> [, <from_srid>], <to_srid>)
```

## Argumenty

| Argumenty     | Opis                                                                                                                                                      |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| `<geometry>`  | Argument musi być wyrażeniem typu obiektu GEOMETRY.                                                                                                       |
| `<from_srid>` | Opcjonalny identyfikator SRID wskazujący bieżący SRS wejściowego obiektu GEOMETRY; jeśli ten argument zostanie pominięty, używany jest SRID określony w wejściowym obiekcie GEOMETRY. |
| `<to_srid>`   | Identyfikator SRID wskazujący SRS, który ma zostać użyty; funkcja przekształca wejściowy obiekt GEOMETRY w nowy obiekt używający tego SRS.                |

## Typ zwracany

Geometry.

## Przykłady SQL

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
