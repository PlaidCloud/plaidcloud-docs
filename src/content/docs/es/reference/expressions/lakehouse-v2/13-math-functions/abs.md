---
title: ABS (Lakehouse v2)
description: ABS — devuelve el valor absoluto de un número.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/abs.md
---

Devuelve el valor absoluto de un número.

## Sintaxis de Analyze

```python
func.abs(<x>)
```

## Ejemplos de Analyze

```python
func.abs(-5)

┌───┐
│ 5  │
└───┘
```

## Sintaxis de SQL

```sql
ABS(<x>)
```

## Ejemplos de SQL

```sql
SELECT ABS(-5);

┌───┐
│ 5  │
└───┘
```
