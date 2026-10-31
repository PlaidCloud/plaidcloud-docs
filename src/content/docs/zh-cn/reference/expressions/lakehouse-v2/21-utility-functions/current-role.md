---
title: CURRENT_ROLE (Lakehouse v2)
description: CURRENT_ROLE：返回当前处于活动状态的角色。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/current-role.md
---

返回当前处于活动状态的角色。

## Analyze 语法

```python
func.current_role()
```

## Analyze 示例

```python
func.current_role()

┌─────────┐
│ 'admin'  │
└─────────┘
```

## SQL 语法

```sql
CURRENT_ROLE()
```

## SQL 示例

```sql
SELECT CURRENT_ROLE();

┌───────┐
│ admin  │
└───────┘
```
