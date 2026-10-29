---
title: HAVERSINE (Lakehouse v1)
description: HAVERSINE — oblicza odległość ortodromiczną w kilometrach między dwoma punktami na powierzchni Ziemi za pomocą wzoru haversine.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/haversine.md
---

Oblicza odległość ortodromiczną w kilometrach między dwoma punktami na powierzchni Ziemi za pomocą [wzoru haversine](https://en.wikipedia.org/wiki/Haversine_formula). Oba punkty są określone przez szerokość i długość geograficzną w stopniach.

## Składnia SQL

```sql
HAVERSINE(<lat1>, <lon1>, <lat2>, <lon2>)
```

## Argumenty

| Argumenty | Opis                               |
|-----------|------------------------------------|
| `<lat1>`  | Szerokość geograficzna pierwszego punktu. |
| `<lon1>`  | Długość geograficzna pierwszego punktu.   |
| `<lat2>`  | Szerokość geograficzna drugiego punktu.   |
| `<lon2>`  | Długość geograficzna drugiego punktu.     |

## Typ zwracany

Double.

## Przykłady SQL

```sql
SELECT
  HAVERSINE(40.7127, -74.0059, 34.0500, -118.2500) AS distance

┌────────────────┐
│    distance    │
├────────────────┤
│ 3936.390533556 │
└────────────────┘
```
