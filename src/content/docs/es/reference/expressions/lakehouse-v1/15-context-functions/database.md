---
title: DATABASE (Lakehouse v1)
description: DATABASE devuelve el nombre de la base de datos seleccionada actualmente.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/15-context-functions/database.md
---

Devuelve el nombre de la base de datos seleccionada actualmente. Si no hay ninguna base de datos seleccionada, esta función devuelve `default`.

## Sintaxis de Analyze

```python
func.database()
```

## Ejemplos de Analyze

```python
func.database()

┌─────────────────┐
│ func.database() │
├─────────────────┤
│ default         │
└─────────────────┘
```

## Sintaxis de SQL

```sql
DATABASE()
```

## Ejemplos de SQL

```sql
SELECT DATABASE();

┌────────────┐
│ database() │
├────────────┤
│ default    │
└────────────┘
```
