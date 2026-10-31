---
title: ARRAY_CONTAINS_SEQ (Lakehouse v2)
description: ARRAY_CONTAINS_SEQ — vérifie si un tableau contient tous les éléments d'un autre tableau dans le même ordre.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-contains-seq.md
---

Vérifie si un tableau contient tous les éléments d'un autre tableau dans le même ordre.

## Syntaxe Analyze

```python
func.array_contains_seq([1,2,3], [1,2])
```

## Exemples Analyze

```python
func.array_contains_seq([1, 2, 3, 4], [2, 3])

┌───┐
│ 1 │
└───┘
```

## Syntaxe SQL

```sql
ARRAY_CONTAINS_SEQ([1,2,3], [1,2])
```

## Exemples SQL

```sql
SELECT ARRAY_CONTAINS_SEQ([1, 2, 3, 4], [2, 3]);

┌───┐
│ 1 │
└───┘
```
