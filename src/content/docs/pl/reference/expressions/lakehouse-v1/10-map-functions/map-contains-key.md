---
title: MAP_CONTAINS_KEY (Lakehouse v1)
description: MAP_CONTAINS_KEY — określa, czy podana mapa (MAP) zawiera podany klucz.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-contains-key.md
---

Określa, czy podana mapa (MAP) zawiera podany klucz.

## Składnia SQL

```sql
MAP_CONTAINS_KEY( <map>, <key> )
```

## Argumenty

| Argumenty | Opis                        |
|-----------|-----------------------------|
| `<map>`   | Przeszukiwana mapa.         |
| `<key>`   | Klucz do znalezienia.       |

## Typ zwracany

Boolean.

## Przykłady SQL

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
