---
title: MAP_DELETE (Lakehouse v1)
description: MAP_DELETE — renvoie un MAP existant dont une ou plusieurs clés ont été supprimées.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-delete.md
---

Renvoie un MAP existant dont une ou plusieurs clés ont été supprimées.

## Syntaxe SQL

```sql
MAP_DELETE( <map>, <key1> [, <key2>, ... ] )
MAP_DELETE( <map>, <array> )
```

## Arguments

| Arguments | Description                                            |
|-----------|--------------------------------------------------------|
| `<map>`   | Le MAP qui contient la KEY à supprimer.                |
| `<keyN>`  | Les KEY à omettre du MAP renvoyé.                      |
| `<array>` | Le tableau de KEY à omettre du MAP renvoyé.            |

:::note
- Les types des expressions de clé et des clés du map doivent être identiques.
- Les valeurs de clé introuvables dans le map sont ignorées.
:::

## Type de retour

Map.

## Exemples SQL

```sql
SELECT MAP_DELETE({'a':1,'b':2,'c':3}, 'a', 'c');
┌───────────────────────────────────────────┐
│ map_delete({'a':1,'b':2,'c':3}, 'a', 'c') │
├───────────────────────────────────────────┤
│ {'b':2}                                   │
└───────────────────────────────────────────┘

SELECT MAP_DELETE({'a':1,'b':2,'c':3}, ['a', 'b']);
┌─────────────────────────────────────────────┐
│ map_delete({'a':1,'b':2,'c':3}, ['a', 'b']) │
├─────────────────────────────────────────────┤
│ {'c':3}                                     │
└─────────────────────────────────────────────┘
```
