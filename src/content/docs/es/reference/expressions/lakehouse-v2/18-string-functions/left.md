---
title: LEFT (Lakehouse v2)
description: LEFT — Devuelve los primeros N caracteres de una cadena, contando desde la izquierda.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/left.md
---

Devuelve los primeros N caracteres de una cadena, contando desde la izquierda.

## Sintaxis de Analyze

```python
func.left(<str>, <len>)
```

## Ejemplos de Analyze

```python
func.left('StarRocks', 4)

┌────────┐
│ 'Star'  │
└────────┘
```

## Sintaxis de SQL

```sql
LEFT(<str>, <len>)
```

## Ejemplos de SQL

```sql
SELECT LEFT('StarRocks', 4);

┌──────┐
│ Star  │
└──────┘
```
