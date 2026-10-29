---
title: MAP_KEYS (Lakehouse v1)
description: MAP_KEYS — gibt die Schlüssel einer Map zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-keys.md
---

Gibt die Schlüssel einer Map zurück.

## SQL-Syntax

```sql
MAP_KEYS( <map> )
```

## Argumente

| Argumente | Beschreibung       |
|-----------|--------------------|
| `<map>`   | Die Eingabe-Map.   |

## Rückgabetyp

Array.

## SQL-Beispiele

```sql
SELECT MAP_KEYS({'a':1,'b':2,'c':3});

┌───────────────────────────────┐
│ map_keys({'a':1,'b':2,'c':3}) │
├───────────────────────────────┤
│ ['a','b','c']                 │
└───────────────────────────────┘
```
