---
title: MAP_VALUES (Lakehouse v1)
description: MAP_VALUES — renvoie les valeurs d'un map.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-values.md
---

Renvoie les valeurs d'un map.

## Syntaxe SQL

```sql
MAP_VALUES( <map> )
```

## Arguments

| Arguments | Description        |
|-----------|--------------------|
| `<map>`   | Le map en entrée.  |

## Type de retour

Array.

## Exemples SQL

```sql
SELECT MAP_VALUES({'a':1,'b':2,'c':3});

┌─────────────────────────────────┐
│ map_values({'a':1,'b':2,'c':3}) │
├─────────────────────────────────┤
│ [1,2,3]                         │
└─────────────────────────────────┘
```
