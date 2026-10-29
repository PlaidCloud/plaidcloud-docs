---
title: MAP_PICK (Lakehouse v1)
description: MAP_PICK — devuelve un MAP nuevo que contiene los pares clave-valor especificados de un MAP existente.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-pick.md
---

Devuelve un MAP nuevo que contiene los pares clave-valor especificados de un MAP existente.

## Sintaxis de SQL

```sql
MAP_PICK( <map>, <key1> [, <key2>, ... ] )
MAP_PICK( <map>, <array> )
```

## Argumentos

| Argumentos | Descripción                                             |
|-----------|-------------------------------------------------------- |
| `<map>`   | El MAP de entrada.                                          |
| `<keyN>`  | Las claves que se incluyen en el MAP devuelto.          |
| `<array>` | La matriz de claves que se incluyen en el MAP devuelto. |

:::note
- Los tipos de las expresiones de clave y de las claves del mapa deben ser los mismos.
- Los valores de clave que no se encuentren en el mapa se ignoran.
:::

## Tipo de valor devuelto

Mapa.

## Ejemplos de SQL

```sql
SELECT MAP_PICK({'a':1,'b':2,'c':3}, 'a', 'c');
┌─────────────────────────────────────────┐
│ map_pick({'a':1,'b':2,'c':3}, 'a', 'c') │
├─────────────────────────────────────────┤
│ {'a':1,'c':3}                           │
└─────────────────────────────────────────┘

SELECT MAP_PICK({'a':1,'b':2,'c':3}, ['a', 'b']);
┌───────────────────────────────────────────┐
│ map_pick({'a':1,'b':2,'c':3}, ['a', 'b']) │
├───────────────────────────────────────────┤
│ {'a':1,'b':2}                             │
└───────────────────────────────────────────┘
```
