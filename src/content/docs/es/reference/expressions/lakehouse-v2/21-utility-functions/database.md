---
title: DATABASE (Lakehouse v2)
description: DATABASE — Devuelve el nombre de la base de datos actual.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/database.md
---

Devuelve el nombre de la base de datos actual.

## Sintaxis de Analyze

```python
func.database()
```

## Ejemplos de Analyze

```python
func.database()

┌───────────────┐
│ 'my_database'  │
└───────────────┘
```

## Sintaxis de SQL

```sql
DATABASE()
```

## Ejemplos de SQL

```sql
SELECT DATABASE();

┌─────────────┐
│ my_database  │
└─────────────┘
```
