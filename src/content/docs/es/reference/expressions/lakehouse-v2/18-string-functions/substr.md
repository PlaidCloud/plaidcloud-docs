---
title: SUBSTR (Lakehouse v2)
description: SUBSTR — Devuelve una subcadena a partir de una posición especificada con una longitud opcional.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/substr.md
---

Devuelve una subcadena a partir de una posición especificada con una longitud opcional.

## Sintaxis de Analyze

```python
func.substr(<str>, <pos>[, <len>])
```

## Ejemplos de Analyze

```python
func.substr('StarRocks', 5, 5)

┌─────────┐
│ 'Rocks'  │
└─────────┘
```

## Sintaxis de SQL

```sql
SUBSTR(<str>, <pos>[, <len>])
```

## Ejemplos de SQL

```sql
SELECT SUBSTR('StarRocks', 5, 5);

┌───────┐
│ Rocks  │
└───────┘
```
