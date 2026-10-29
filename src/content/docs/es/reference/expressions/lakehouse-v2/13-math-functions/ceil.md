---
title: CEIL (Lakehouse v2)
description: CEIL — devuelve el entero más pequeño mayor o igual que un número.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/ceil.md
---

Devuelve el entero más pequeño mayor o igual que un número.

## Sintaxis de Analyze

```python
func.ceil(<x>)
```

## Ejemplos de Analyze

```python
func.ceil(3.2)

┌───┐
│ 4  │
└───┘
```

## Sintaxis de SQL

```sql
CEIL(<x>)
```

## Ejemplos de SQL

```sql
SELECT CEIL(3.2);

┌───┐
│ 4  │
└───┘
```
