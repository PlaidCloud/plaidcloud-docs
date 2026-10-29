---
title: RIGHT (Lakehouse v2)
description: RIGHT — Devuelve los últimos N caracteres de una cadena, contando desde la derecha.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/right.md
---

Devuelve los últimos N caracteres de una cadena, contando desde la derecha.

## Sintaxis de Analyze

```python
func.right(<str>, <len>)
```

## Ejemplos de Analyze

```python
func.right('StarRocks', 5)

┌─────────┐
│ 'Rocks'  │
└─────────┘
```

## Sintaxis de SQL

```sql
RIGHT(<str>, <len>)
```

## Ejemplos de SQL

```sql
SELECT RIGHT('StarRocks', 5);

┌───────┐
│ Rocks  │
└───────┘
```
