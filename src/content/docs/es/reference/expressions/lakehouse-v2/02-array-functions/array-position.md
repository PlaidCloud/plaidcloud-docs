---
title: ARRAY_POSITION (Lakehouse v2)
description: ARRAY_POSITION — devuelve la posición de la primera aparición de un elemento (índice basado en 1).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-position.md
---

Devuelve la posición de la primera aparición de un elemento (índice basado en 1).

## Sintaxis de Analyze

```python
func.array_position([10, 20, 30], 20)
```

## Ejemplos de Analyze

```python
func.array_position([10, 20, 30], 20)

┌───┐
│ 2 │
└───┘
```

## Sintaxis de SQL

```sql
ARRAY_POSITION([10, 20, 30], 20)
```

## Ejemplos de SQL

```sql
SELECT ARRAY_POSITION([10, 20, 30], 20);

┌───┐
│ 2 │
└───┘
```
