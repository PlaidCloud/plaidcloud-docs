---
title: SUB_BITMAP (Lakehouse v1)
description: "SUB_BITMAP : génère un sous-bitmap du bitmap source, à partir de l'indice de début, avec une taille donnée."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/sub-bitmap.md
---

Génère un sous-bitmap du bitmap source, à partir de l'indice de début, avec une taille donnée.

## Syntaxe Analyze

```python
func.sub_bitmap( <bitmap>, <start>, <size> )
```

## Exemples Analyze

```python
func.sub_bitmap(func.build_bitmap([1, 2, 3, 4, 5]), 1, 3)

┌───────────────────────────────────────────────────────────┐
│ func.sub_bitmap(func.build_bitmap([1, 2, 3, 4, 5]), 1, 3) │
├───────────────────────────────────────────────────────────┤
│ 2,3,4                                                     │
└───────────────────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
SUB_BITMAP( <bitmap>, <start>, <size> )
```

## Exemples SQL

```sql
SELECT SUB_BITMAP(BUILD_BITMAP([1, 2, 3, 4, 5]), 1, 3)::String;

┌─────────────────────────────────────────────────────────┐
│ sub_bitmap(build_bitmap([1, 2, 3, 4, 5]), 1, 3)::string │
├─────────────────────────────────────────────────────────┤
│ 2,3,4                                                   │
└─────────────────────────────────────────────────────────┘
```
