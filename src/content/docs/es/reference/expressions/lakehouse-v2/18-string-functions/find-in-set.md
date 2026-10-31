---
title: FIND_IN_SET (Lakehouse v2)
description: FIND_IN_SET — Devuelve la posición de una cadena dentro de una lista separada por comas.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/find-in-set.md
---

Devuelve la posición de una cadena dentro de una lista separada por comas.

## Sintaxis de Analyze

```python
func.find_in_set(<str>, <strlist>)
```

## Ejemplos de Analyze

```python
func.find_in_set('b', 'a,b,c')

┌───┐
│ 2  │
└───┘
```

## Sintaxis de SQL

```sql
FIND_IN_SET(<str>, <strlist>)
```

## Ejemplos de SQL

```sql
SELECT FIND_IN_SET('b', 'a,b,c');

┌───┐
│ 2  │
└───┘
```
