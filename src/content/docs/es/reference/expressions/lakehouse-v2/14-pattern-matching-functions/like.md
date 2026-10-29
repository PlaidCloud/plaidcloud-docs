---
title: LIKE (Lakehouse v2)
description: "Use la función de coincidencia de patrones LIKE en PlaidCloud Lakehouse. Compara una cadena con un patrón mediante `%` (cualquier carácter) y `_` (un solo carácter)."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/14-pattern-matching-functions/like.md
---

Compara una cadena con un patrón mediante los comodines `%` (cualquier carácter) y `_` (un solo carácter).

## Sintaxis de Analyze

```python
func.like(<str> LIKE <pattern>)
```

## Ejemplos de Analyze

```python
get_column(table, 'name').like('%alice%')

┌───────────┐
│ (boolean)  │
└───────────┘
```

## Sintaxis de SQL

```sql
LIKE(<str> LIKE <pattern>)
```

## Ejemplos de SQL

```sql
SELECT name FROM users WHERE name LIKE '%alice%';

┌─────────────┐
│ alice_smith  │
└─────────────┘
```
