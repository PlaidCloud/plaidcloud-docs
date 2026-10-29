---
title: MAP_INSERT (Lakehouse v1)
description: MAP_INSERT — zwraca nową mapę (MAP) składającą się z mapy wejściowej z wstawioną nową parą klucz-wartość (lub zaktualizowanym istniejącym kluczem).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-insert.md
---

Zwraca nową mapę (MAP) składającą się z mapy wejściowej z wstawioną nową parą klucz-wartość (istniejący klucz zostaje zaktualizowany nową wartością).

## Składnia SQL

```sql
MAP_INSERT( <map>, <key>, <value> [, <updateFlag> ] )
```

## Argumenty

| Argumenty      | Opis                                                                                         |
|----------------|----------------------------------------------------------------------------------------------|
| `<map>`        | Wejściowa mapa (MAP).                                                                        |
| `<key>`        | Nowy klucz do wstawienia do mapy.                                                            |
| `<value>`      | Nowa wartość do wstawienia do mapy.                                                          |
| `<updateFlag>` | Flaga logiczna wskazująca, czy istniejący klucz może zostać nadpisany. Wartość domyślna to FALSE. |

## Typ zwracany

Map.

## Przykłady SQL

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
