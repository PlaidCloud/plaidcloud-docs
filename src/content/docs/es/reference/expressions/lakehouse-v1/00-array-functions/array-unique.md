---
title: ARRAY_UNIQUE (Lakehouse v1)
description: ARRAY_UNIQUE — cuenta los elementos únicos del arreglo (excepto NULL).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-unique.md
---

Cuenta los elementos únicos del arreglo (excepto NULL).

## Sintaxis de Analyze

```python
func.array_unique( <array> )
```

## Ejemplos de Analyze

```python
func.array_unique([1, 2, 3, 3, 4])

┌─────────────────────────────────────┐
│ func.array_unique([1, 2, 3, 3, 4])  │
├─────────────────────────────────────┤
│                                   4 │
└─────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
ARRAY_UNIQUE( <array> )
```

## Ejemplos de SQL

```sql
SELECT ARRAY_UNIQUE([1, 2, 3, 3, 4]);

┌───────────────────────────────┐
│ array_unique([1, 2, 3, 3, 4]) │
├───────────────────────────────┤
│                             4 │
└───────────────────────────────┘
```
