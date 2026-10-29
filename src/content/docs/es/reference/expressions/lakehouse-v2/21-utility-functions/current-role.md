---
title: CURRENT_ROLE (Lakehouse v2)
description: CURRENT_ROLE — Devuelve el rol activo actual.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/current-role.md
---

Devuelve el rol activo actual.

## Sintaxis de Analyze

```python
func.current_role()
```

## Ejemplos de Analyze

```python
func.current_role()

┌─────────┐
│ 'admin'  │
└─────────┘
```

## Sintaxis de SQL

```sql
CURRENT_ROLE()
```

## Ejemplos de SQL

```sql
SELECT CURRENT_ROLE();

┌───────┐
│ admin  │
└───────┘
```
