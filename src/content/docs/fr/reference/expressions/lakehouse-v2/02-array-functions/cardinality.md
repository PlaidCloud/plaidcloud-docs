---
title: "CARDINALITY (tableau, Lakehouse v2)"
description: CARDINALITY — renvoie le nombre d'éléments d'un tableau. Alias de `ARRAY_LENGTH`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/cardinality.md
---

Renvoie le nombre d'éléments d'un tableau. Alias de `ARRAY_LENGTH`.

## Syntaxe Analyze

```python
func.cardinality([1, 2, 3])
```

## Exemples Analyze

```python
func.cardinality([10, 20, 30])

┌───┐
│ 3 │
└───┘
```

## Syntaxe SQL

```sql
CARDINALITY([1, 2, 3])
```

## Exemples SQL

```sql
SELECT CARDINALITY([10, 20, 30]);

┌───┐
│ 3 │
└───┘
```
