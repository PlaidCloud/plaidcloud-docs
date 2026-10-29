---
title: IS_ROLE_IN_SESSION（Lakehouse v2）
description: IS_ROLE_IN_SESSION — 指定したロールが現在のセッションでアクティブかどうかを判定します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/is-role-in-session.md
---

指定したロールが現在のセッションでアクティブかどうかを判定します。

## Analyze 構文

```python
func.is_role_in_session(<role_name>)
```

## Analyze の例

```python
func.is_role_in_session('admin')

┌──────┐
│ True  │
└──────┘
```

## SQL 構文

```sql
IS_ROLE_IN_SESSION(<role_name>)
```

## SQL の例

```sql
SELECT IS_ROLE_IN_SESSION('admin');

┌───┐
│ 1  │
└───┘
```
