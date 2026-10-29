---
title: ARRAY_PREPEND (Lakehouse v1)
description: ARRAY_PREPEND — antepone un elemento al arreglo.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-prepend.md
---

Antepone un elemento al arreglo.

## Sintaxis de Analyze

```python
func.array_prepend( <element>, <array> )
```

## Ejemplos de Analyze

```python
func.array_prepend(1, [3, 4])

┌────────────────────────────────┐
│ func.array_prepend(1, [3, 4])  │
├────────────────────────────────┤
│ [1,3,4]                        │
└────────────────────────────────┘
```

## Sintaxis de SQL

```sql
ARRAY_PREPEND( <element>, <array> )
```

## Ejemplos de SQL

```sql
SELECT ARRAY_PREPEND(1, [3, 4]);

┌──────────────────────────┐
│ array_prepend(1, [3, 4]) │
├──────────────────────────┤
│ [1,3,4]                  │
└──────────────────────────┘
```
