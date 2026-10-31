---
title: ARRAY_POSITION (Lakehouse v2)
description: ARRAY_POSITION — renvoie la position de la première occurrence d'un élément (indexation à partir de 1).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-position.md
---

Renvoie la position de la première occurrence d'un élément (indexation à partir de 1).

## Syntaxe Analyze

```python
func.array_position([10, 20, 30], 20)
```

## Exemples Analyze

```python
func.array_position([10, 20, 30], 20)

┌───┐
│ 2 │
└───┘
```

## Syntaxe SQL

```sql
ARRAY_POSITION([10, 20, 30], 20)
```

## Exemples SQL

```sql
SELECT ARRAY_POSITION([10, 20, 30], 20);

┌───┐
│ 2 │
└───┘
```
