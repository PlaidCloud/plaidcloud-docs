---
title: LEAST (Lakehouse v2)
description: LEAST — renvoie la plus petite valeur d'une liste de valeurs.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/least.md
---

Renvoie la plus petite valeur d'une liste de valeurs.

## Syntaxe Analyze

```python
func.least(<val1>, <val2>[, ...])
```

## Exemples Analyze

```python
func.least(3, 7, 1, 9, 4)

┌───┐
│ 1  │
└───┘
```

## Syntaxe SQL

```sql
LEAST(<val1>, <val2>[, ...])
```

## Exemples SQL

```sql
SELECT LEAST(3, 7, 1, 9, 4);

┌───┐
│ 1  │
└───┘
```
