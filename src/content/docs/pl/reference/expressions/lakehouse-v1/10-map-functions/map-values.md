---
title: MAP_VALUES (Lakehouse v1)
description: MAP_VALUES — zwraca wartości z mapy.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-values.md
---

Zwraca wartości z mapy.

## Składnia SQL

```sql
MAP_VALUES( <map> )
```

## Argumenty

| Argumenty | Opis                |
|-----------|---------------------|
| `<map>`   | Mapa wejściowa.     |

## Typ zwracany

Array.

## Przykłady SQL

```sql
SELECT MAP_VALUES({'a':1,'b':2,'c':3});

┌─────────────────────────────────┐
│ map_values({'a':1,'b':2,'c':3}) │
├─────────────────────────────────┤
│ [1,2,3]                         │
└─────────────────────────────────┘
```
