---
title: MAP_SIZE (Lakehouse v1)
description: MAP_SIZE — gibt die Größe einer MAP zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-size.md
---

Gibt die Größe einer MAP zurück.

## SQL-Syntax

```sql
MAP_SIZE( <map> )
```

## Argumente

| Argumente | Beschreibung       |
|-----------|--------------------|
| `<map>`   | Die Eingabe-Map.   |

## Rückgabetyp

UInt64.

## SQL-Beispiele

```sql
SELECT MAP_SIZE({'a':1,'b':2,'c':3});

┌───────────────────────────────┐
│ map_size({'a':1,'b':2,'c':3}) │
├───────────────────────────────┤
│ 3                             │
└───────────────────────────────┘
```
