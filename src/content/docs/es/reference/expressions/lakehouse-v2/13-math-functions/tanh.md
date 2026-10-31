---
title: TANH (Lakehouse v2)
description: TANH — devuelve la tangente hiperbólica de un número.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/tanh.md
---

Devuelve la tangente hiperbólica de un número.

## Sintaxis de Analyze

```python
func.tanh(<x>)
```

## Ejemplos de Analyze

```python
func.tanh(0)

┌─────┐
│ 0.0  │
└─────┘
```

## Sintaxis de SQL

```sql
TANH(<x>)
```

## Ejemplos de SQL

```sql
SELECT TANH(0);

┌─────┐
│ 0.0  │
└─────┘
```
