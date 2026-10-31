---
title: CURRENT_USER (Lakehouse v1)
description: CURRENT_USER：返回服务器用于验证当前客户端的账户的用户名和主机名组合。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/15-context-functions/current-user.md
---

返回服务器用于验证当前客户端的账户的用户名和主机名组合。该账户决定您的访问权限。返回值是 utf8 字符集的字符串。

## Analyze 语法

```python
func.current_user()
```

## Analyze 示例

```python
func.current_user()

┌─────────────────────┐
│ func.current_user() │
├─────────────────────┤
│ 'root'@'%'          │
└─────────────────────┘
```

## SQL 语法

```sql
CURRENT_USER()
```

## SQL 示例

```sql
SELECT CURRENT_USER();

┌────────────────┐
│ current_user() │
├────────────────┤
│ 'root'@'%'     │
└────────────────┘
```
