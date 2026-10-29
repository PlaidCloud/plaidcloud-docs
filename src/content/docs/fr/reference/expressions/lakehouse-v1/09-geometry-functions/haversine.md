---
title: HAVERSINE (Lakehouse v1)
description: HAVERSINE — calcule la distance orthodromique, en kilomètres, entre deux points de la surface de la Terre à l'aide de la formule de Haversine.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/haversine.md
---

Calcule la distance orthodromique, en kilomètres, entre deux points de la surface de la Terre à l'aide de la [formule de Haversine](https://en.wikipedia.org/wiki/Haversine_formula). Les deux points sont définis par leur latitude et leur longitude, en degrés.

## Syntaxe SQL

```sql
HAVERSINE(<lat1>, <lon1>, <lat2>, <lon2>)
```

## Arguments

| Arguments | Description                        |
|-----------|------------------------------------|
| `<lat1>`  | La latitude du premier point.      |
| `<lon1>`  | La longitude du premier point.     |
| `<lat2>`  | La latitude du second point.       |
| `<lon2>`  | La longitude du second point.      |

## Type de retour

Double.

## Exemples SQL

```sql
SELECT
  HAVERSINE(40.7127, -74.0059, 34.0500, -118.2500) AS distance

┌────────────────┐
│    distance    │
├────────────────┤
│ 3936.390533556 │
└────────────────┘
```
