---
title: REGEXP (Lakehouse v2)
description: REGEXP — 检查字符串是否与正则表达式模式匹配。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/14-pattern-matching-functions/regexp.md
---

检查字符串是否与正则表达式模式匹配。

## Analyze 语法

```python
func.regexp(<str> REGEXP <pattern>)
```

## Analyze 示例

```python
get_column(table, 'email').regexp_match('^[a-z]+@')

┌───────────┐
│ (boolean)  │
└───────────┘
```

## SQL 语法

```sql
REGEXP(<str> REGEXP <pattern>)
```

## SQL 示例

```sql
SELECT email FROM users WHERE email REGEXP '^[a-z]+@[a-z]+\\.com$';

┌───────────────────┐
│ alice@example.com  │
└───────────────────┘
```
