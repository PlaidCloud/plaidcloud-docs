---
title: ARRAY_REPEAT (Lakehouse v2)
description: ARRAY_REPEAT — crea una matriz que contiene un elemento específico repetido N veces.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-repeat.md
---

Crea una matriz que contiene un elemento específico repetido N veces.

## Sintaxis de Analyze

```python
func.array_repeat('x', 3)
```

## Ejemplos de Analyze

```python
func.array_repeat('x', 3)

┌───────────────┐
│ ['x','x','x'] │
└───────────────┘
```

## Sintaxis de SQL

```sql
ARRAY_REPEAT('x', 3)
```

## Ejemplos de SQL

```sql
SELECT ARRAY_REPEAT('x', 3);

┌───────────────┐
│ ["x","x","x"] │
└───────────────┘
```
