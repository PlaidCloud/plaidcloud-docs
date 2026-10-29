---
title: FACTORIAL (Lakehouse v1)
description: FACTORIAL — devuelve el factorial de x.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/factorial.md
---

Devuelve el factorial de `x`. Si `x` es menor o igual que 0, la función devuelve 0.

## Sintaxis de Analyze

```python
func.factorial( <x> )
```

## Ejemplos de Analyze

```python
func.factorial(5)

┌───────────────────┐
│ func.factorial(5) │
├───────────────────┤
│               120 │
└───────────────────┘
```

## Sintaxis de SQL

```sql
FACTORIAL( <x> )
```

## Ejemplos de SQL

```sql
SELECT FACTORIAL(5);

┌──────────────┐
│ factorial(5) │
├──────────────┤
│          120 │
└──────────────┘
```
