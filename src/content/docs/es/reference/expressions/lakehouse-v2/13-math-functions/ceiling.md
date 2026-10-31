---
title: CEILING (Lakehouse v2)
description: CEILING — devuelve el entero más pequeño mayor o igual que un número. Alias de `CEIL`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/ceiling.md
---

Devuelve el entero más pequeño mayor o igual que un número. Alias de `CEIL`.

## Sintaxis de Analyze

```python
func.ceiling(<x>)
```

## Ejemplos de Analyze

```python
func.ceiling(3.2)

┌───┐
│ 4  │
└───┘
```

## Sintaxis de SQL

```sql
CEILING(<x>)
```

## Ejemplos de SQL

```sql
SELECT CEILING(3.2);

┌───┐
│ 4  │
└───┘
```
