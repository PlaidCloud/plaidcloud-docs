---
title: MAP_INSERT (Lakehouse v1)
description: MAP_INSERT — devuelve un MAP nuevo formado por el MAP de entrada con un nuevo par clave-valor insertado (o una clave existente actualizada con un valor nuevo).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-insert.md
---

Devuelve un MAP nuevo formado por el MAP de entrada con un nuevo par clave-valor insertado (o una clave existente actualizada con un valor nuevo).

## Sintaxis de SQL

```sql
MAP_INSERT( <map>, <key>, <value> [, <updateFlag> ] )
```

## Argumentos

| Argumentos     | Descripción                                                                                  |
|----------------|----------------------------------------------------------------------------------------------|
| `<map>`        | El MAP de entrada.                                                                               |
| `<key>`        | La nueva clave que se inserta en el MAP.                                                          |
| `<value>`      | El nuevo valor que se inserta en el MAP.                                                        |
| `<updateFlag>` | La marca booleana indica si se puede sobrescribir una clave existente. El valor predeterminado es FALSE. |

## Tipo de valor devuelto

Mapa.

## Ejemplos de SQL

```sql
SELECT MAP_INSERT({'a':1,'b':2,'c':3}, 'd', 4);
┌─────────────────────────────────────────┐
│ map_insert({'a':1,'b':2,'c':3}, 'd', 4) │
├─────────────────────────────────────────┤
│ {'a':1,'b':2,'c':3,'d':4}               │
└─────────────────────────────────────────┘

SELECT MAP_INSERT({'a':1,'b':2,'c':3}, 'a', 5, true);
┌───────────────────────────────────────────────┐
│ map_insert({'a':1,'b':2,'c':3}, 'a', 5, TRUE) │
├───────────────────────────────────────────────┤
│ {'a':5,'b':2,'c':3}                           │
└───────────────────────────────────────────────┘
```
