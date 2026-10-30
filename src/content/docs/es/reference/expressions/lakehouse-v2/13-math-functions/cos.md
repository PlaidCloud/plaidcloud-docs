---
title: COS (Lakehouse v2)
description: COS — devuelve el coseno de un número en radianes.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/cos.md
---

Devuelve el coseno de un número en radianes.

## Sintaxis de Analyze

```python
func.cos(<x>)
```

## Ejemplos de Analyze

```python
func.cos(0)

┌─────┐
│ 1.0  │
└─────┘
```

## Sintaxis de SQL

```sql
COS(<x>)
```

## Ejemplos de SQL

```sql
SELECT COS(0);

┌─────┐
│ 1.0  │
└─────┘
```
