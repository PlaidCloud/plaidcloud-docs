---
title: FIELD (Lakehouse v2)
description: FIELD — Devuelve la posición de índice de un valor en una lista de argumentos.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/field.md
---

Devuelve la posición de índice de un valor en una lista de argumentos.

## Sintaxis de Analyze

```python
func.field(<str>, <val1>, <val2>[, ...])
```

## Ejemplos de Analyze

```python
func.field('b', 'a', 'b', 'c')

┌───┐
│ 2  │
└───┘
```

## Sintaxis de SQL

```sql
FIELD(<str>, <val1>, <val2>[, ...])
```

## Ejemplos de SQL

```sql
SELECT FIELD('b', 'a', 'b', 'c');

┌───┐
│ 2  │
└───┘
```
