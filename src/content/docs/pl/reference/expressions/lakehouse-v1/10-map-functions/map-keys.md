---
title: MAP_KEYS (Lakehouse v1)
description: MAP_KEYS — zwraca klucze z mapy.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-keys.md
---

Zwraca klucze z mapy.

## Składnia SQL

```sql
MAP_KEYS( <map> )
```

## Argumenty

| Argumenty | Opis                |
|-----------|---------------------|
| `<map>`   | Mapa wejściowa.     |

## Typ zwracany

Array.

## Przykłady SQL

```sql
SELECT MAP_KEYS({'a':1,'b':2,'c':3});

┌───────────────────────────────┐
│ map_keys({'a':1,'b':2,'c':3}) │
├───────────────────────────────┤
│ ['a','b','c']                 │
└───────────────────────────────┘
```
