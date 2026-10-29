---
title: DIV0 (Lakehouse v1)
description: DIV0 — renvoie le quotient de la division du premier nombre par le second.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/div0.md
---

Renvoie le quotient de la division du premier nombre par le second. Renvoie 0 si le second nombre est 0.

Voir aussi :

- [DIV](../div)
- [DIVNULL](../divnull)

## Syntaxe Analyze

```python
func.div0(<numerator>, <denominator>)
```

## Exemples Analyze

```python
func.div0(20, 6), func.div0(20, 0), func.div0(20, null)

┌─────────────────────────────────────────────────────────────┐
│  func.div0(20, 6)  │ func.div0(20, 0) │ func.div0(20, null) │
├────────────────────┼──────────────────┼─────────────────────┤
│ 3.3333333333333335 │                0 │ NULL                │
└─────────────────────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
DIV0(<number1>, <number2>)
```

## Exemples SQL

```sql
SELECT
  DIV0(20, 6),
  DIV0(20, 0),
  DIV0(20, NULL);

┌───────────────────────────────────────────────────┐
│     div0(20, 6)    │ div0(20, 0) │ div0(20, null) │
├────────────────────┼─────────────┼────────────────┤
│ 3.3333333333333335 │           0 │ NULL           │
└───────────────────────────────────────────────────┘
```
