---
title: HAVERSINE (Lakehouse v1)
description: HAVERSINE — calcula a distância ortodrómica em quilómetros entre dois pontos da superfície da Terra, utilizando a fórmula de Haversine.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/haversine.md
---

Calcula a distância ortodrómica em quilómetros entre dois pontos da superfície da Terra, utilizando a [fórmula de Haversine](https://en.wikipedia.org/wiki/Haversine_formula). Os dois pontos são especificados pela respetiva latitude e longitude, em graus.

## Sintaxe SQL

```sql
HAVERSINE(<lat1>, <lon1>, <lat2>, <lon2>)
```

## Argumentos

| Argumentos | Descrição                          |
|-----------|------------------------------------|
| `<lat1>`  | A latitude do primeiro ponto.      |
| `<lon1>`  | A longitude do primeiro ponto.     |
| `<lat2>`  | A latitude do segundo ponto.       |
| `<lon2>`  | A longitude do segundo ponto.      |

## Tipo de retorno

Double.

## Exemplos de SQL

```sql
SELECT
  HAVERSINE(40.7127, -74.0059, 34.0500, -118.2500) AS distance

┌────────────────┐
│    distance    │
├────────────────┤
│ 3936.390533556 │
└────────────────┘
```
