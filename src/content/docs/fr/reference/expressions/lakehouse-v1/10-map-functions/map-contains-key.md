---
title: MAP_CONTAINS_KEY (Lakehouse v1)
description: MAP_CONTAINS_KEY — détermine si le MAP indiqué contient la clé indiquée.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-contains-key.md
---

Détermine si le MAP indiqué contient la clé indiquée.

## Syntaxe SQL

```sql
MAP_CONTAINS_KEY( <map>, <key> )
```

## Arguments

| Arguments | Description             |
|-----------|-------------------------|
| `<map>`   | Le map à parcourir.     |
| `<key>`   | La clé à rechercher.    |

## Type de retour

Boolean.

## Exemples SQL

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
