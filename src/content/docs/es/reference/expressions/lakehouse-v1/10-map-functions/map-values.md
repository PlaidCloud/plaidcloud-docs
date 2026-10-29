---
title: MAP_VALUES (Lakehouse v1)
description: MAP_VALUES — devuelve los valores de un mapa.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-values.md
---

Devuelve los valores de un mapa.

## Sintaxis de SQL

```sql
MAP_VALUES( <map> )
```

## Argumentos

| Argumentos | Descripción    |
|-----------|----------------|
| `<map>`   | El mapa de entrada. |

## Tipo de valor devuelto

Matriz.

## Ejemplos de SQL

```sql
SELECT MAP_VALUES({'a':1,'b':2,'c':3});

┌─────────────────────────────────┐
│ map_values({'a':1,'b':2,'c':3}) │
├─────────────────────────────────┤
│ [1,2,3]                         │
└─────────────────────────────────┘
```
