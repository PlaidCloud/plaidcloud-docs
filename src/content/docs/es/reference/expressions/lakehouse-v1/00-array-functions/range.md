---
title: RANGE (Lakehouse v1)
description: RANGE — devuelve un arreglo formado por los valores del intervalo [start, end).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/range.md
---

Devuelve un arreglo formado por los valores del intervalo [start, end).

## Sintaxis de Analyze

```python
func.range( <start>, <end> )
```

## Ejemplos de Sqanalyzel

```python
func.range(1, 5)

┌────────────────────┐
│  func.range(1, 5)  │
├────────────────────┤
│ [1,2,3,4]          │
└────────────────────┘
```

## Sintaxis de SQL

```sql
RANGE( <start>, <end> )
```

## Ejemplos de SQL

```sql
SELECT RANGE(1, 5);

┌───────────────┐
│  range(1, 5)  │
├───────────────┤
│ [1,2,3,4]     │
└───────────────┘
```
