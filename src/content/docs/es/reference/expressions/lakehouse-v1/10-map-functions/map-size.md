---
title: MAP_SIZE (Lakehouse v1)
description: MAP_SIZE — devuelve el tamaño de un MAP.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-size.md
---

Devuelve el tamaño de un MAP.

## Sintaxis de SQL

```sql
MAP_SIZE( <map> )
```

## Argumentos

| Argumentos | Descripción    |
|-----------|----------------|
| `<map>`   | El mapa de entrada. |

## Tipo de valor devuelto

UInt64.

## Ejemplos de SQL

```sql
SELECT MAP_SIZE({'a':1,'b':2,'c':3});

┌───────────────────────────────┐
│ map_size({'a':1,'b':2,'c':3}) │
├───────────────────────────────┤
│ 3                             │
└───────────────────────────────┘
```
