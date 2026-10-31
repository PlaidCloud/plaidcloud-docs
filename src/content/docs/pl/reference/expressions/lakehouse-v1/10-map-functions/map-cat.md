---
title: MAP_CAT (Lakehouse v1)
description: MAP_CAT — zwraca złączenie dwóch map (MAP).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-cat.md
---

Zwraca złączenie dwóch map (MAP).

## Składnia SQL

```sql
MAP_CAT( <map1>, <map2> )
```

## Argumenty

| Argumenty | Opis                            |
|-----------|---------------------------------|
| `<map1>`  | Mapa źródłowa (MAP).            |
| `<map2>`  | Mapa (MAP) dołączana do map1.   |

:::note
- Jeśli zarówno map1, jak i map2 zawierają wartość o tym samym kluczu, mapa wynikowa zawiera wartość z map2.
- Jeśli którykolwiek argument ma wartość NULL, funkcja zwraca NULL bez zgłaszania błędu.
:::

## Typ zwracany

Map.

## Przykłady SQL

```sql
SELECT MAP_CAT({'a':1,'b':2,'c':3}, {'c':5,'d':6});
┌─────────────────────────────────────────────┐
│ map_cat({'a':1,'b':2,'c':3}, {'c':5,'d':6}) │
├─────────────────────────────────────────────┤
│ {'a':1,'b':2,'c':5,'d':6}                   │
└─────────────────────────────────────────────┘
```
