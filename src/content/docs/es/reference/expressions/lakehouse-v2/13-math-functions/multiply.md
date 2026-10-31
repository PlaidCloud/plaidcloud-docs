---
title: MULTIPLY (Lakehouse v2)
description: MULTIPLY — devuelve el producto de dos números.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/multiply.md
---

Devuelve el producto de dos números.

## Sintaxis de Analyze

```python
func.multiply(<x>, <y>)
```

## Ejemplos de Analyze

```python
func.multiply(6, 7)

┌────┐
│ 42  │
└────┘
```

## Sintaxis de SQL

```sql
MULTIPLY(<x>, <y>)
```

## Ejemplos de SQL

```sql
SELECT MULTIPLY(6, 7);

┌────┐
│ 42  │
└────┘
```
