---
title: MAP_DELETE (Lakehouse v1)
description: MAP_DELETE — zwraca istniejącą mapę (MAP) z usuniętym jednym lub kilkoma kluczami.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-delete.md
---

Zwraca istniejącą mapę (MAP) z usuniętym jednym lub kilkoma kluczami.

## Składnia SQL

```sql
MAP_DELETE( <map>, <key1> [, <key2>, ... ] )
MAP_DELETE( <map>, <array> )
```

## Argumenty

| Argumenty | Opis                                                   |
|-----------|--------------------------------------------------------|
| `<map>`   | Mapa (MAP) zawierająca klucz (KEY) do usunięcia.       |
| `<keyN>`  | Klucze (KEY) do pominięcia w zwracanej mapie.          |
| `<array>` | Tablica kluczy (KEY) do pominięcia w zwracanej mapie.  |

:::note
- Typy wyrażeń kluczy i kluczy w mapie muszą być takie same.
- Wartości kluczy, których nie ma w mapie, są ignorowane.
:::

## Typ zwracany

Map.

## Przykłady SQL

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
