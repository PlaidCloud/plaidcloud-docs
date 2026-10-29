---
title: IS_ROLE_IN_SESSION (Lakehouse v2)
description: IS_ROLE_IN_SESSION — Comprueba si un rol especificado está activo en la sesión actual.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/is-role-in-session.md
---

Comprueba si un rol especificado está activo en la sesión actual.

## Sintaxis de Analyze

```python
func.is_role_in_session(<role_name>)
```

## Ejemplos de Analyze

```python
func.is_role_in_session('admin')

┌──────┐
│ True  │
└──────┘
```

## Sintaxis de SQL

```sql
IS_ROLE_IN_SESSION(<role_name>)
```

## Ejemplos de SQL

```sql
SELECT IS_ROLE_IN_SESSION('admin');

┌───┐
│ 1  │
└───┘
```
