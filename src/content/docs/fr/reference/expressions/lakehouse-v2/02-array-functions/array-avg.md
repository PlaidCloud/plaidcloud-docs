---
title: ARRAY_AVG (Lakehouse v2)
description: ARRAY_AVG — renvoie la moyenne des éléments d'un tableau.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-avg.md
---

Renvoie la moyenne des éléments d'un tableau.

## Syntaxe Analyze

```python
func.array_avg([1, 2, 3, 4])
```

## Exemples Analyze

```python
func.array_avg([10, 20, 30])

┌──────┐
│ 20.0 │
└──────┘
```

## Syntaxe SQL

```sql
ARRAY_AVG([1, 2, 3, 4])
```

## Exemples SQL

```sql
SELECT ARRAY_AVG([10, 20, 30]);

┌──────┐
│ 20.0 │
└──────┘
```
