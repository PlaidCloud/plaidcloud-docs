---
title: MAP_DELETE (Lakehouse v1)
description: MAP_DELETE — devuelve un MAP existente con una o más claves eliminadas.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-delete.md
---

Devuelve un MAP existente con una o más claves eliminadas.

## Sintaxis de SQL

```sql
MAP_DELETE( <map>, <key1> [, <key2>, ... ] )
MAP_DELETE( <map>, <array> )
```

## Argumentos

| Argumentos | Descripción                                            |
|-----------|--------------------------------------------------------|
| `<map>`   | El MAP que contiene la clave que se va a eliminar.               |
| `<keyN>`  | Las claves que se omiten del MAP devuelto.          |
| `<array>` | La matriz de claves que se omiten del MAP devuelto. |

:::note
- Los tipos de las expresiones de clave y de las claves del mapa deben ser los mismos.
- Los valores de clave que no se encuentren en el mapa se ignoran.
:::

## Tipo de valor devuelto

Mapa.

## Ejemplos de SQL

```sql
SELECT MAP_DELETE({'a':1,'b':2,'c':3}, 'a', 'c');
┌───────────────────────────────────────────┐
│ map_delete({'a':1,'b':2,'c':3}, 'a', 'c') │
├───────────────────────────────────────────┤
│ {'b':2}                                   │
└───────────────────────────────────────────┘

SELECT MAP_DELETE({'a':1,'b':2,'c':3}, ['a', 'b']);
┌─────────────────────────────────────────────┐
│ map_delete({'a':1,'b':2,'c':3}, ['a', 'b']) │
├─────────────────────────────────────────────┤
│ {'c':3}                                     │
└─────────────────────────────────────────────┘
```
