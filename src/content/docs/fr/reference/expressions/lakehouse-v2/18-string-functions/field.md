---
title: FIELD (Lakehouse v2)
description: FIELD — renvoie la position d'une valeur dans une liste d'arguments.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/field.md
---

Renvoie la position d'une valeur dans une liste d'arguments.

## Syntaxe Analyze

```python
func.field(<str>, <val1>, <val2>[, ...])
```

## Exemples Analyze

```python
func.field('b', 'a', 'b', 'c')

┌───┐
│ 2  │
└───┘
```

## Syntaxe SQL

```sql
FIELD(<str>, <val1>, <val2>[, ...])
```

## Exemples SQL

```sql
SELECT FIELD('b', 'a', 'b', 'c');

┌───┐
│ 2  │
└───┘
```
