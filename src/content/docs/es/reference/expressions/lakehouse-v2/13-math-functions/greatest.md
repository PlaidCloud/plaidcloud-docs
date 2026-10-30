---
title: GREATEST (Lakehouse v2)
description: GREATEST — devuelve el valor más grande de una lista de valores.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/greatest.md
---

Devuelve el valor más grande de una lista de valores.

## Sintaxis de Analyze

```python
func.greatest(<val1>, <val2>[, ...])
```

## Ejemplos de Analyze

```python
func.greatest(3, 7, 1, 9, 4)

┌───┐
│ 9  │
└───┘
```

## Sintaxis de SQL

```sql
GREATEST(<val1>, <val2>[, ...])
```

## Ejemplos de SQL

```sql
SELECT GREATEST(3, 7, 1, 9, 4);

┌───┐
│ 9  │
└───┘
```
