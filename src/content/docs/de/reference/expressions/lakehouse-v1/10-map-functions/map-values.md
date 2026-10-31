---
title: MAP_VALUES (Lakehouse v1)
description: MAP_VALUES — gibt die Werte einer Map zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-values.md
---

Gibt die Werte einer Map zurück.

## SQL-Syntax

```sql
MAP_VALUES( <map> )
```

## Argumente

| Argumente | Beschreibung       |
|-----------|--------------------|
| `<map>`   | Die Eingabe-Map.   |

## Rückgabetyp

Array.

## SQL-Beispiele

```sql
SELECT MAP_VALUES({'a':1,'b':2,'c':3});

┌─────────────────────────────────┐
│ map_values({'a':1,'b':2,'c':3}) │
├─────────────────────────────────┤
│ [1,2,3]                         │
└─────────────────────────────────┘
```
