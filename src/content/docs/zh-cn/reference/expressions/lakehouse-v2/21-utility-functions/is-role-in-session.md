---
title: IS_ROLE_IN_SESSION (Lakehouse v2)
description: IS_ROLE_IN_SESSION：检查指定角色在当前会话中是否处于活动状态。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/is-role-in-session.md
---

检查指定角色在当前会话中是否处于活动状态。

## Analyze 语法

```python
func.is_role_in_session(<role_name>)
```

## Analyze 示例

```python
func.is_role_in_session('admin')

┌──────┐
│ True  │
└──────┘
```

## SQL 语法

```sql
IS_ROLE_IN_SESSION(<role_name>)
```

## SQL 示例

```sql
SELECT IS_ROLE_IN_SESSION('admin');

┌───┐
│ 1  │
└───┘
```
