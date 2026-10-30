---
title: MAP_INSERT (Lakehouse v1)
description: MAP_INSERT — renvoie un nouveau MAP composé du MAP en entrée dans lequel une nouvelle paire clé-valeur est insérée (ou une clé existante mise à jour avec une nouvelle valeur).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-insert.md
---

Renvoie un nouveau MAP composé du MAP en entrée dans lequel une nouvelle paire clé-valeur est insérée (ou une clé existante mise à jour avec une nouvelle valeur).

## Syntaxe SQL

```sql
MAP_INSERT( <map>, <key>, <value> [, <updateFlag> ] )
```

## Arguments

| Arguments      | Description                                                                                  |
|----------------|----------------------------------------------------------------------------------------------|
| `<map>`        | Le MAP en entrée.                                                                            |
| `<key>`        | La nouvelle clé à insérer dans le MAP.                                                       |
| `<value>`      | La nouvelle valeur à insérer dans le MAP.                                                    |
| `<updateFlag>` | L'indicateur booléen précise si une clé existante peut être écrasée. La valeur par défaut est FALSE. |

## Type de retour

Map.

## Exemples SQL

```sql
SELECT MAP_INSERT({'a':1,'b':2,'c':3}, 'd', 4);
┌─────────────────────────────────────────┐
│ map_insert({'a':1,'b':2,'c':3}, 'd', 4) │
├─────────────────────────────────────────┤
│ {'a':1,'b':2,'c':3,'d':4}               │
└─────────────────────────────────────────┘

SELECT MAP_INSERT({'a':1,'b':2,'c':3}, 'a', 5, true);
┌───────────────────────────────────────────────┐
│ map_insert({'a':1,'b':2,'c':3}, 'a', 5, TRUE) │
├───────────────────────────────────────────────┤
│ {'a':5,'b':2,'c':3}                           │
└───────────────────────────────────────────────┘
```
