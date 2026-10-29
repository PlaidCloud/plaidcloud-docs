---
title: ARRAY_CONTAINS_ALL (Lakehouse v2)
description: ARRAY_CONTAINS_ALL — vérifie si un tableau contient tous les éléments d'un autre tableau.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-contains-all.md
---

Vérifie si un tableau contient tous les éléments d'un autre tableau.

## Syntaxe Analyze

```python
func.array_contains_all([1,2,3], [1,2])
```

## Exemples Analyze

```python
func.array_contains_all([1, 2, 3], [1, 2])

┌───┐
│ 1 │
└───┘
```

## Syntaxe SQL

```sql
ARRAY_CONTAINS_ALL([1,2,3], [1,2])
```

## Exemples SQL

```sql
SELECT ARRAY_CONTAINS_ALL([1, 2, 3], [1, 2]);

┌───┐
│ 1 │
└───┘
```
