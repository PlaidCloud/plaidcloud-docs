---
title: MAP_PICK (Lakehouse v1)
description: MAP_PICK — zwraca nową mapę (MAP) zawierającą podane pary klucz-wartość z istniejącej mapy.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-pick.md
---

Zwraca nową mapę (MAP) zawierającą podane pary klucz-wartość z istniejącej mapy.

## Składnia SQL

```sql
MAP_PICK( <map>, <key1> [, <key2>, ... ] )
MAP_PICK( <map>, <array> )
```

## Argumenty

| Argumenty | Opis                                                    |
|-----------|-------------------------------------------------------- |
| `<map>`   | Wejściowa mapa (MAP).                                   |
| `<keyN>`  | Klucze (KEY) do uwzględnienia w zwracanej mapie.        |
| `<array>` | Tablica kluczy (KEY) do uwzględnienia w zwracanej mapie. |

:::note
- Typy wyrażeń kluczy i kluczy w mapie muszą być takie same.
- Wartości kluczy, których nie ma w mapie, są ignorowane.
:::

## Typ zwracany

Map.

## Przykłady SQL

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
