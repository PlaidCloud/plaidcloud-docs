---
title: IS_ROLE_IN_SESSION (Lakehouse v2)
description: IS_ROLE_IN_SESSION — prüft, ob eine angegebene Rolle in der aktuellen Sitzung aktiv ist.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/is-role-in-session.md
---

Prüft, ob eine angegebene Rolle in der aktuellen Sitzung aktiv ist.

## Analyze-Syntax

```python
func.is_role_in_session(<role_name>)
```

## Analyze-Beispiele

```python
func.is_role_in_session('admin')

┌──────┐
│ True  │
└──────┘
```

## SQL-Syntax

```sql
IS_ROLE_IN_SESSION(<role_name>)
```

## SQL-Beispiele

```sql
SELECT IS_ROLE_IN_SESSION('admin');

┌───┐
│ 1  │
└───┘
```
