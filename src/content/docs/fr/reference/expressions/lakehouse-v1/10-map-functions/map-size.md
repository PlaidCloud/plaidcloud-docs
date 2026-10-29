---
title: MAP_SIZE (Lakehouse v1)
description: MAP_SIZE — renvoie la taille d'un MAP.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-size.md
---

Renvoie la taille d'un MAP.

## Syntaxe SQL

```sql
MAP_SIZE( <map> )
```

## Arguments

| Arguments | Description        |
|-----------|--------------------|
| `<map>`   | Le map en entrée.  |

## Type de retour

UInt64.

## Exemples SQL

```sql
SELECT MAP_SIZE({'a':1,'b':2,'c':3});

┌───────────────────────────────┐
│ map_size({'a':1,'b':2,'c':3}) │
├───────────────────────────────┤
│ 3                             │
└───────────────────────────────┘
```
