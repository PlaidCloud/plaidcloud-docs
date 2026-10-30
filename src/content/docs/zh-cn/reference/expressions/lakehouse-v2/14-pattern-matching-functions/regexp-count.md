---
title: REGEXP_COUNT (Lakehouse v2)
description: "在 PlaidCloud Lakehouse 中使用 REGEXP_COUNT 模式匹配函数。返回正则表达式模式在字符串中出现的次数。"
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/14-pattern-matching-functions/regexp-count.md
---

返回正则表达式模式在字符串中出现的次数。

## Analyze 语法

```python
func.regexp_count(<str>, <pattern>)
```

## Analyze 示例

```python
func.regexp_count('banana', 'an')

┌───┐
│ 2  │
└───┘
```

## SQL 语法

```sql
REGEXP_COUNT(<str>, <pattern>)
```

## SQL 示例

```sql
SELECT REGEXP_COUNT('banana', 'an');

┌───┐
│ 2  │
└───┘
```
