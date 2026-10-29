---
title: MODULO (Lakehouse v1)
description: MODULO — retorna o resto da divisão de x por y.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/modulo.md
---

Retorna o resto da divisão de `x` por `y`. Se `y` for 0, retorna um erro.

## Sintaxe do Analyze

```python
func.modulo( <x>, <y> )
```

## Exemplos do Analyze

```python
func.modulo(9, 2)

┌───────────────────┐
│ func.modulo(9, 2) │
├───────────────────┤
│                 1 │
└───────────────────┘
```

## Sintaxe SQL

```sql
MODULO( <x>, <y> )
```

## Aliases

- [MOD](../mod)

## Exemplos de SQL

```sql
SELECT MOD(9, 2), MODULO(9, 2);

┌──────────────────────────┐
│ mod(9, 2) │ modulo(9, 2) │
├───────────┼──────────────┤
│         1 │            1 │
└──────────────────────────┘
```
