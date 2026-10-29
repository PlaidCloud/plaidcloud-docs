---
title: ARRAY_SORT (Lakehouse v1)
description: "ARRAY_SORT : trie les éléments du tableau par ordre croissant."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-sort.md
---

Trie les éléments du tableau par ordre croissant.

## Syntaxe Analyze

```sql
func.array_sort( <array>[, <order>, <nullposition>] )
```

| Paramètre    | Par défaut  | Description                                                                                                                                    |
|--------------|-------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| order        | ASC         | Indique l'ordre de tri, croissant (ASC) ou décroissant (DESC).                                                                                 |
| nullposition | NULLS FIRST | Détermine la position des valeurs NULL dans le résultat du tri : au début (NULLS FIRST) ou à la fin (NULLS LAST) de la sortie triée.           |

## Exemples Analyze

```sql
func.array_sort([1, 4, 3, 2])

┌────────────────────────────────┐
│ func.array_sort([1, 4, 3, 2])  │
├────────────────────────────────┤
│ [1,2,3,4]                      │
└────────────────────────────────┘
```

## Syntaxe SQL

```sql
ARRAY_SORT( <array>[, <order>, <nullposition>] )
```

| Paramètre    | Par défaut  | Description                                                                                                                                    |
|--------------|-------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| order        | ASC         | Indique l'ordre de tri, croissant (ASC) ou décroissant (DESC).                                                                                 |
| nullposition | NULLS FIRST | Détermine la position des valeurs NULL dans le résultat du tri : au début (NULLS FIRST) ou à la fin (NULLS LAST) de la sortie triée.           |

## Exemples SQL

```sql
SELECT ARRAY_SORT([1, 4, 3, 2]);

┌──────────────────────────┐
│ array_sort([1, 4, 3, 2]) │
├──────────────────────────┤
│ [1,2,3,4]                │
└──────────────────────────┘
```
