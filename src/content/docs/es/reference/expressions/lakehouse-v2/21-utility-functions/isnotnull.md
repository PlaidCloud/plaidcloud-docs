---
title: ISNOTNULL (Lakehouse v2)
description: ISNOTNULL — Comprueba si un valor no es NULL. Devuelve 1 si no es NULL y 0 en caso contrario.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/isnotnull.md
---

Comprueba si un valor no es NULL. Devuelve 1 si no es NULL y 0 en caso contrario.

## Sintaxis de Analyze

```python
func.isnotnull(<expr>)
```

## Ejemplos de Analyze

```python
func.isnotnull(1)

┌───┐
│ 1  │
└───┘
```

## Sintaxis de SQL

```sql
ISNOTNULL(<expr>)
```

## Ejemplos de SQL

```sql
SELECT ISNOTNULL(1);

┌───┐
│ 1  │
└───┘
```
