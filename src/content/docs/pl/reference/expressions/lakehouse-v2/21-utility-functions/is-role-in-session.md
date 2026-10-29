---
title: IS_ROLE_IN_SESSION (Lakehouse v2)
description: IS_ROLE_IN_SESSION — sprawdza, czy podana rola jest aktywna w bieżącej sesji.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/is-role-in-session.md
---

Sprawdza, czy podana rola jest aktywna w bieżącej sesji.

## Składnia Analyze

```python
func.is_role_in_session(<role_name>)
```

## Przykłady Analyze

```python
func.is_role_in_session('admin')

┌──────┐
│ True  │
└──────┘
```

## Składnia SQL

```sql
IS_ROLE_IN_SESSION(<role_name>)
```

## Przykłady SQL

```sql
SELECT IS_ROLE_IN_SESSION('admin');

┌───┐
│ 1  │
└───┘
```
