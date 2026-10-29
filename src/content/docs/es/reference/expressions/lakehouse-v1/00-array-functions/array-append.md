---
title: ARRAY_APPEND (Lakehouse v1)
description: ARRAY_APPEND — antepone un elemento al arreglo.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-append.md
---

Antepone un elemento al arreglo.

## Sintaxis de Analyze

```python
func.array_append( <array>, <element>)
```

## Ejemplos de Analyze

```python
func.array_append([3, 4], 5)

┌──────────────────────────────┐
│ func.array_append([3, 4], 5) │
├──────────────────────────────┤
│ [3,4,5]                      │
└──────────────────────────────┘
```

## Sintaxis de SQL

```sql
ARRAY_APPEND( <array>, <element>)
```

## Ejemplos de SQL

```sql
SELECT ARRAY_APPEND([3, 4], 5);

┌─────────────────────────┐
│ array_append([3, 4], 5) │
├─────────────────────────┤
│ [3,4,5]                 │
└─────────────────────────┘
```
