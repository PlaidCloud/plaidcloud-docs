---
title: LOG2 (Lakehouse v2)
description: LOG2 — devuelve el logaritmo en base 2 de un número.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/log2.md
---

Devuelve el logaritmo en base 2 de un número.

## Sintaxis de Analyze

```python
func.log2(<x>)
```

## Ejemplos de Analyze

```python
func.log2(8)

┌─────┐
│ 3.0  │
└─────┘
```

## Sintaxis de SQL

```sql
LOG2(<x>)
```

## Ejemplos de SQL

```sql
SELECT LOG2(8);

┌─────┐
│ 3.0  │
└─────┘
```
