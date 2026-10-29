---
title: STARTS_WITH (Lakehouse v2)
description: STARTS_WITH — Comprueba si una cadena comienza con un prefijo especificado.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/starts-with.md
---

Comprueba si una cadena comienza con un prefijo especificado.

## Sintaxis de Analyze

```python
func.starts_with(<str>, <prefix>)
```

## Ejemplos de Analyze

```python
func.starts_with('StarRocks', 'Star')

┌───┐
│ 1  │
└───┘
```

## Sintaxis de SQL

```sql
STARTS_WITH(<str>, <prefix>)
```

## Ejemplos de SQL

```sql
SELECT STARTS_WITH('StarRocks', 'Star');

┌───┐
│ 1  │
└───┘
```
