---
title: MODULO (Lakehouse v1)
description: MODULO — renvoie le reste de la division de x par y.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/modulo.md
---

Renvoie le reste de la division de `x` par `y`. Si `y` vaut 0, elle renvoie une erreur.

## Syntaxe Analyze

```python
func.modulo( <x>, <y> )
```

## Exemples Analyze

```python
func.modulo(9, 2)

┌───────────────────┐
│ func.modulo(9, 2) │
├───────────────────┤
│                 1 │
└───────────────────┘
```

## Syntaxe SQL

```sql
MODULO( <x>, <y> )
```

## Alias

- [MOD](../mod)

## Exemples SQL

```sql
SELECT MOD(9, 2), MODULO(9, 2);

┌──────────────────────────┐
│ mod(9, 2) │ modulo(9, 2) │
├───────────┼──────────────┤
│         1 │            1 │
└──────────────────────────┘
```
