---
title: ISNULL (Lakehouse v2)
description: ISNULL — Comprueba si un valor es NULL. Devuelve 1 si es NULL y 0 en caso contrario.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/isnull.md
---

Comprueba si un valor es NULL. Devuelve 1 si es NULL y 0 en caso contrario.

## Sintaxis de Analyze

```python
func.isnull(<expr>)
```

## Ejemplos de Analyze

```python
func.isnull(None)

┌───┐
│ 1  │
└───┘
```

## Sintaxis de SQL

```sql
ISNULL(<expr>)
```

## Ejemplos de SQL

```sql
SELECT ISNULL(NULL);

┌───┐
│ 1  │
└───┘
```
