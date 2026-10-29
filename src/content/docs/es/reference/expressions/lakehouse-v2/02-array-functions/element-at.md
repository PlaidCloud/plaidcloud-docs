---
title: "ELEMENT_AT (Matriz, Lakehouse v2)"
description: ELEMENT_AT — devuelve el elemento situado en una posición específica de una matriz (índice basado en 1).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/element-at.md
---

Devuelve el elemento situado en una posición específica de una matriz (índice basado en 1).

## Sintaxis de Analyze

```python
func.element_at([10, 20, 30], 2)
```

## Ejemplos de Analyze

```python
func.element_at([10, 20, 30], 2)

┌────┐
│ 20 │
└────┘
```

## Sintaxis de SQL

```sql
ELEMENT_AT([10, 20, 30], 2)
```

## Ejemplos de SQL

```sql
SELECT ELEMENT_AT([10, 20, 30], 2);

┌────┐
│ 20 │
└────┘
```
