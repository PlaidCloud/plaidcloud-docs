---
title: IS_ROLE_IN_SESSION (Lakehouse v2)
description: IS_ROLE_IN_SESSION — verifica se uma função especificada está ativa na sessão atual.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/is-role-in-session.md
---

Verifica se uma função especificada está ativa na sessão atual.

## Sintaxe do Analyze

```python
func.is_role_in_session(<role_name>)
```

## Exemplos do Analyze

```python
func.is_role_in_session('admin')

┌──────┐
│ True  │
└──────┘
```

## Sintaxe SQL

```sql
IS_ROLE_IN_SESSION(<role_name>)
```

## Exemplos de SQL

```sql
SELECT IS_ROLE_IN_SESSION('admin');

┌───┐
│ 1  │
└───┘
```
