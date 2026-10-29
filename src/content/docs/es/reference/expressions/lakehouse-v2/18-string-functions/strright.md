---
title: STRRIGHT (Lakehouse v2)
description: STRRIGHT — Devuelve los últimos N caracteres de una cadena, contando desde la derecha. Alias de `RIGHT`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/strright.md
---

Devuelve los últimos N caracteres de una cadena, contando desde la derecha. Alias de `RIGHT`.

## Sintaxis de Analyze

```python
func.strright(<str>, <len>)
```

## Ejemplos de Analyze

```python
func.strright('StarRocks', 5)

┌─────────┐
│ 'Rocks'  │
└─────────┘
```

## Sintaxis de SQL

```sql
STRRIGHT(<str>, <len>)
```

## Ejemplos de SQL

```sql
SELECT STRRIGHT('StarRocks', 5);

┌───────┐
│ Rocks  │
└───────┘
```
