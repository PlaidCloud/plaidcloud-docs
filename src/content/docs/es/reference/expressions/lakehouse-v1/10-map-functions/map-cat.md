---
title: MAP_CAT (Lakehouse v1)
description: MAP_CAT — devuelve la concatenación de dos MAP.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-cat.md
---

Devuelve la concatenación de dos MAP.

## Sintaxis de SQL

```sql
MAP_CAT( <map1>, <map2> )
```

## Argumentos

| Argumentos | Descripción                     |
|-----------|---------------------------------|
| `<map1>`  | El MAP de origen.                 |
| `<map2>`  | El MAP que se anexa a map1. |

:::note
- Si map1 y map2 tienen un valor con la misma clave, el mapa de salida contiene el valor de map2.
- Si alguno de los argumentos es NULL, la función devuelve NULL sin notificar ningún error.
:::

## Tipo de valor devuelto

Mapa.

## Ejemplos de SQL

```sql
SELECT MAP_CAT({'a':1,'b':2,'c':3}, {'c':5,'d':6});
┌─────────────────────────────────────────────┐
│ map_cat({'a':1,'b':2,'c':3}, {'c':5,'d':6}) │
├─────────────────────────────────────────────┤
│ {'a':1,'b':2,'c':5,'d':6}                   │
└─────────────────────────────────────────────┘
```
