---
title: ST_SETSRID (Lakehouse v1)
description: ST_SETSRID — zwraca obiekt GEOMETRY z ustawionym identyfikatorem SRID (identyfikator układu odniesienia przestrzennego).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-setsrid.md
---

Zwraca obiekt GEOMETRY, którego [SRID (identyfikator układu odniesienia przestrzennego)](https://en.wikipedia.org/wiki/Spatial_reference_system#Identifier) ustawiono na podaną wartość. Ta funkcja zmienia wyłącznie SRID i nie wpływa na współrzędne obiektu. Jeśli trzeba również zmienić współrzędne tak, aby odpowiadały nowemu układowi odniesienia przestrzennego (SRS), użyj zamiast niej funkcji [ST_TRANSFORM](../st-transform).

## Składnia SQL

```sql
ST_SETSRID(<geometry>, <srid>)
```

## Argumenty

| Argumenty    | Opis                                                        |
|--------------|-------------------------------------------------------------|
| `<geometry>` | Argument musi być wyrażeniem typu obiektu GEOMETRY.         |
| `<srid>`     | Liczba całkowita SRID ustawiana w zwracanym obiekcie GEOMETRY. |

## Typ zwracany

Geometry.

## Przykłady SQL

```sql
SET GEOMETRY_OUTPUT_FORMAT = 'EWKT'

SELECT ST_SETSRID(TO_GEOMETRY('POINT(13 51)'), 4326) AS geometry

┌────────────────────────┐
│        geometry        │
├────────────────────────┤
│ SRID=4326;POINT(13 51) │
└────────────────────────┘

```
