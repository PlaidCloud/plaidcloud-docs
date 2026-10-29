---
title: HAVERSINE (Lakehouse v1)
description: HAVERSINE — calcula la distancia de círculo máximo en kilómetros entre dos puntos de la superficie terrestre mediante la fórmula del haversine.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/haversine.md
---

Calcula la distancia de círculo máximo en kilómetros entre dos puntos de la superficie terrestre mediante la [fórmula del haversine](https://en.wikipedia.org/wiki/Haversine_formula). Los dos puntos se especifican por su latitud y longitud en grados.

## Sintaxis de SQL

```sql
HAVERSINE(<lat1>, <lon1>, <lat2>, <lon2>)
```

## Argumentos

| Argumentos | Descripción                        |
|-----------|------------------------------------|
| `<lat1>`  | La latitud del primer punto.   |
| `<lon1>`  | La longitud del primer punto.  |
| `<lat2>`  | La latitud del segundo punto.  |
| `<lon2>`  | La longitud del segundo punto. |

## Tipo de valor devuelto

Doble.

## Ejemplos de SQL

```sql
SELECT
  HAVERSINE(40.7127, -74.0059, 34.0500, -118.2500) AS distance

┌────────────────┐
│    distance    │
├────────────────┤
│ 3936.390533556 │
└────────────────┘
```
