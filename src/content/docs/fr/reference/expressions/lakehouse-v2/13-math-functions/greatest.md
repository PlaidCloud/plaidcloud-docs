---
title: GREATEST (Lakehouse v2)
description: GREATEST — renvoie la plus grande valeur d'une liste de valeurs.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/greatest.md
---

Renvoie la plus grande valeur d'une liste de valeurs.

## Syntaxe Analyze

```python
func.greatest(<val1>, <val2>[, ...])
```

## Exemples Analyze

```python
func.greatest(3, 7, 1, 9, 4)

┌───┐
│ 9  │
└───┘
```

## Syntaxe SQL

```sql
GREATEST(<val1>, <val2>[, ...])
```

## Exemples SQL

```sql
SELECT GREATEST(3, 7, 1, 9, 4);

┌───┐
│ 9  │
└───┘
```
