---
title: MAP_CAT (Lakehouse v1)
description: MAP_CAT — renvoie la concaténation de deux MAP.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-cat.md
---

Renvoie la concaténation de deux MAP.

## Syntaxe SQL

```sql
MAP_CAT( <map1>, <map2> )
```

## Arguments

| Arguments | Description                     |
|-----------|---------------------------------|
| `<map1>`  | Le MAP source.                  |
| `<map2>`  | Le MAP à ajouter à map1.        |

:::note
- Si map1 et map2 contiennent une valeur pour la même clé, le map en sortie contient la valeur de map2.
- Si l'un des arguments est NULL, la fonction renvoie NULL sans signaler d'erreur.
:::

## Type de retour

Map.

## Exemples SQL

```sql
SELECT MAP_CAT({'a':1,'b':2,'c':3}, {'c':5,'d':6});
┌─────────────────────────────────────────────┐
│ map_cat({'a':1,'b':2,'c':3}, {'c':5,'d':6}) │
├─────────────────────────────────────────────┤
│ {'a':1,'b':2,'c':5,'d':6}                   │
└─────────────────────────────────────────────┘
```
