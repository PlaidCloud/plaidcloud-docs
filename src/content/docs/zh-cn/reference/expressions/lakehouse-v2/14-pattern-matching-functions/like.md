---
title: LIKE (Lakehouse v2)
description: "在 PlaidCloud Lakehouse 中使用 LIKE 模式匹配函数。使用 `%`（任意字符）和 `_`（单个字符）将字符串与模式进行匹配。"
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/14-pattern-matching-functions/like.md
---

使用 `%`（任意字符）和 `_`（单个字符）通配符将字符串与模式进行匹配。

## Analyze 语法

```python
func.like(<str> LIKE <pattern>)
```

## Analyze 示例

```python
get_column(table, 'name').like('%alice%')

┌───────────┐
│ (boolean)  │
└───────────┘
```

## SQL 语法

```sql
LIKE(<str> LIKE <pattern>)
```

## SQL 示例

```sql
SELECT name FROM users WHERE name LIKE '%alice%';

┌─────────────┐
│ alice_smith  │
└─────────────┘
```
