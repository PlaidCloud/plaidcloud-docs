---
title: MAP_CONTAINS_KEY (Lakehouse v1)
description: MAP_CONTAINS_KEY — determina si el MAP especificado contiene la clave especificada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-contains-key.md
---

Determina si el MAP especificado contiene la clave especificada.

## Sintaxis de SQL

```sql
MAP_CONTAINS_KEY( <map>, <key> )
```

## Argumentos

| Argumentos | Descripción             |
|-----------|-------------------------|
| `<map>`   | El mapa en el que se busca. |
| `<key>`   | La clave que se busca.        |

## Tipo de valor devuelto

Booleano.

## Ejemplos de SQL

```sql
SELECT MAP_CONTAINS_KEY({'a':1,'b':2,'c':3}, 'c');
┌────────────────────────────────────────────┐
│ map_contains_key({'a':1,'b':2,'c':3}, 'c') │
├────────────────────────────────────────────┤
│ true                                       │
└────────────────────────────────────────────┘

SELECT MAP_CONTAINS_KEY({'a':1,'b':2,'c':3}, 'x');
┌────────────────────────────────────────────┐
│ map_contains_key({'a':1,'b':2,'c':3}, 'x') │
├────────────────────────────────────────────┤
│ false                                      │
└────────────────────────────────────────────┘
```
