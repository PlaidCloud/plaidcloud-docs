---
title: EXP (Lakehouse v2)
description: EXP — devuelve e elevado a la potencia de un número.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/exp.md
---

Devuelve e elevado a la potencia de un número.

## Sintaxis de Analyze

```python
func.exp(<x>)
```

## Ejemplos de Analyze

```python
func.exp(1)

┌───────────────────┐
│ 2.718281828459045  │
└───────────────────┘
```

## Sintaxis de SQL

```sql
EXP(<x>)
```

## Ejemplos de SQL

```sql
SELECT EXP(1);

┌───────────────────┐
│ 2.718281828459045  │
└───────────────────┘
```
