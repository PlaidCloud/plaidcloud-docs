---
title: ARRAY_CONTAINS (Lakehouse v2)
description: ARRAY_CONTAINS — vérifie si un tableau contient un élément donné.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-contains.md
---

Vérifie si un tableau contient un élément donné.

## Syntaxe Analyze

```python
func.array_contains([1, 2, 3], 2)
```

## Exemples Analyze

```python
func.array_contains([1, 2, 3], 2)

┌───┐
│ 1 │
└───┘
```

## Syntaxe SQL

```sql
ARRAY_CONTAINS([1, 2, 3], 2)
```

## Exemples SQL

```sql
SELECT ARRAY_CONTAINS([1, 2, 3], 2);

┌───┐
│ 1 │
└───┘
```
