---
title: FLOOR (Lakehouse v2)
description: FLOOR — devuelve el entero más grande menor o igual que un número.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/floor.md
---

Devuelve el entero más grande menor o igual que un número.

## Sintaxis de Analyze

```python
func.floor(<x>)
```

## Ejemplos de Analyze

```python
func.floor(3.7)

┌───┐
│ 3  │
└───┘
```

## Sintaxis de SQL

```sql
FLOOR(<x>)
```

## Ejemplos de SQL

```sql
SELECT FLOOR(3.7);

┌───┐
│ 3  │
└───┘
```
