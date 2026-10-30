---
title: MAP_KEYS (Lakehouse v1)
description: MAP_KEYS — renvoie les clés d'un map.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-keys.md
---

Renvoie les clés d'un map.

## Syntaxe SQL

```sql
MAP_KEYS( <map> )
```

## Arguments

| Arguments | Description        |
|-----------|--------------------|
| `<map>`   | Le map en entrée.  |

## Type de retour

Array.

## Exemples SQL

```sql
SELECT MAP_KEYS({'a':1,'b':2,'c':3});

┌───────────────────────────────┐
│ map_keys({'a':1,'b':2,'c':3}) │
├───────────────────────────────┤
│ ['a','b','c']                 │
└───────────────────────────────┘
```
