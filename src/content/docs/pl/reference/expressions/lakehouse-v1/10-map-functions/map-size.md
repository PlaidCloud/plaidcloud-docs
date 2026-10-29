---
title: MAP_SIZE (Lakehouse v1)
description: MAP_SIZE — zwraca rozmiar mapy (MAP).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-size.md
---

Zwraca rozmiar mapy (MAP).

## Składnia SQL

```sql
MAP_SIZE( <map> )
```

## Argumenty

| Argumenty | Opis                |
|-----------|---------------------|
| `<map>`   | Mapa wejściowa.     |

## Typ zwracany

UInt64.

## Przykłady SQL

```sql
SELECT MAP_SIZE({'a':1,'b':2,'c':3});

┌───────────────────────────────┐
│ map_size({'a':1,'b':2,'c':3}) │
├───────────────────────────────┤
│ 3                             │
└───────────────────────────────┘
```
