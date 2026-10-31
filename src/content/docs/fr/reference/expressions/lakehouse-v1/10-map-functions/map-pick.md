---
title: MAP_PICK (Lakehouse v1)
description: MAP_PICK — renvoie un nouveau MAP contenant les paires clé-valeur indiquées d'un MAP existant.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-pick.md
---

Renvoie un nouveau MAP contenant les paires clé-valeur indiquées d'un MAP existant.

## Syntaxe SQL

```sql
MAP_PICK( <map>, <key1> [, <key2>, ... ] )
MAP_PICK( <map>, <array> )
```

## Arguments

| Arguments | Description                                             |
|-----------|-------------------------------------------------------- |
| `<map>`   | Le MAP en entrée.                                       |
| `<keyN>`  | Les KEY à inclure dans le MAP renvoyé.                  |
| `<array>` | Le tableau de KEY à inclure dans le MAP renvoyé.        |

:::note
- Les types des expressions de clé et des clés du map doivent être identiques.
- Les valeurs de clé introuvables dans le map sont ignorées.
:::

## Type de retour

Map.

## Exemples SQL

```sql
SELECT MAP_PICK({'a':1,'b':2,'c':3}, 'a', 'c');
┌─────────────────────────────────────────┐
│ map_pick({'a':1,'b':2,'c':3}, 'a', 'c') │
├─────────────────────────────────────────┤
│ {'a':1,'c':3}                           │
└─────────────────────────────────────────┘

SELECT MAP_PICK({'a':1,'b':2,'c':3}, ['a', 'b']);
┌───────────────────────────────────────────┐
│ map_pick({'a':1,'b':2,'c':3}, ['a', 'b']) │
├───────────────────────────────────────────┤
│ {'a':1,'b':2}                             │
└───────────────────────────────────────────┘
```
