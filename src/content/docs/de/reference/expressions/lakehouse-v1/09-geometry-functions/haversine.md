---
title: HAVERSINE (Lakehouse v1)
description: HAVERSINE — berechnet mit der Haversine-Formel die Großkreisentfernung in Kilometern zwischen zwei Punkten auf der Erdoberfläche.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/haversine.md
---

Berechnet mit der [Haversine-Formel](https://en.wikipedia.org/wiki/Haversine_formula) die Großkreisentfernung in Kilometern zwischen zwei Punkten auf der Erdoberfläche. Die beiden Punkte werden über ihren Breiten- und Längengrad in Grad angegeben.

## SQL-Syntax

```sql
HAVERSINE(<lat1>, <lon1>, <lat2>, <lon2>)
```

## Argumente

| Argumente | Beschreibung                       |
|-----------|------------------------------------|
| `<lat1>`  | Der Breitengrad des ersten Punkts. |
| `<lon1>`  | Der Längengrad des ersten Punkts.  |
| `<lat2>`  | Der Breitengrad des zweiten Punkts.|
| `<lon2>`  | Der Längengrad des zweiten Punkts. |

## Rückgabetyp

Double.

## SQL-Beispiele

```sql
SELECT
  HAVERSINE(40.7127, -74.0059, 34.0500, -118.2500) AS distance

┌────────────────┐
│    distance    │
├────────────────┤
│ 3936.390533556 │
└────────────────┘
```
