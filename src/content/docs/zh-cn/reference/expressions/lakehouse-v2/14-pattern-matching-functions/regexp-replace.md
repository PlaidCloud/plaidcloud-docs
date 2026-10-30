---
title: REGEXP_REPLACE (Lakehouse v2)
description: "在 PlaidCloud Lakehouse 中使用 REGEXP_REPLACE 模式匹配函数。将与正则表达式模式匹配的子字符串替换为指定的替换字符串。"
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/14-pattern-matching-functions/regexp-replace.md
---

将与正则表达式模式匹配的子字符串替换为指定的替换字符串。

## Analyze 语法

```python
func.regexp_replace(<str>, <pattern>, <replacement>)
```

## Analyze 示例

```python
func.regexp_replace('hello   world', '\\s+', ' ')

┌───────────────┐
│ 'hello world'  │
└───────────────┘
```

## SQL 语法

```sql
REGEXP_REPLACE(<str>, <pattern>, <replacement>)
```

## SQL 示例

```sql
SELECT REGEXP_REPLACE('hello   world', '\\s+', ' ');

┌─────────────┐
│ hello world  │
└─────────────┘
```
