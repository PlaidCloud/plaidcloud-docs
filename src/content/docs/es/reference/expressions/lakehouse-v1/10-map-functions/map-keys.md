---
title: MAP_KEYS (Lakehouse v1)
description: MAP_KEYS — devuelve las claves de un mapa.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-keys.md
---

Devuelve las claves de un mapa.

## Sintaxis de SQL

```sql
MAP_KEYS( <map> )
```

## Argumentos

| Argumentos | Descripción    |
|-----------|----------------|
| `<map>`   | El mapa de entrada. |

## Tipo de valor devuelto

Matriz.

## Ejemplos de SQL

```sql
SELECT MAP_KEYS({'a':1,'b':2,'c':3});

┌───────────────────────────────┐
│ map_keys({'a':1,'b':2,'c':3}) │
├───────────────────────────────┤
│ ['a','b','c']                 │
└───────────────────────────────┘
```
