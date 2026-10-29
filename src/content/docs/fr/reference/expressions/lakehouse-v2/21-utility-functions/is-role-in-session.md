---
title: IS_ROLE_IN_SESSION (Lakehouse v2)
description: IS_ROLE_IN_SESSION — vérifie si un rôle donné est actif dans la session courante.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/is-role-in-session.md
---

Vérifie si un rôle donné est actif dans la session courante.

## Syntaxe Analyze

```python
func.is_role_in_session(<role_name>)
```

## Exemples Analyze

```python
func.is_role_in_session('admin')

┌──────┐
│ True  │
└──────┘
```

## Syntaxe SQL

```sql
IS_ROLE_IN_SESSION(<role_name>)
```

## Exemples SQL

```sql
SELECT IS_ROLE_IN_SESSION('admin');

┌───┐
│ 1  │
└───┘
```
