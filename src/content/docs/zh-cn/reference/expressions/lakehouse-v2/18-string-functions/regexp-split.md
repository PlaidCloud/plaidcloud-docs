---
title: REGEXP_SPLIT (Lakehouse v2)
description: REGEXP_SPLIT：按正则表达式模式拆分字符串，并返回子字符串数组。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/regexp-split.md
---

按正则表达式模式拆分字符串，并返回子字符串数组。

## Analyze 语法

```python
func.regexp_split('one1two2three', '[0-9]')
```

## Analyze 示例

```python
func.regexp_split('one1two2three', '[0-9]')

┌───────────────────────┐
│ ["one","two","three"] │
└───────────────────────┘
```

## SQL 语法

```sql
REGEXP_SPLIT(<str>, <pattern>)
```

## SQL 示例

```sql
SELECT REGEXP_SPLIT('one1two2three', '[0-9]');

┌───────────────────────┐
│ ["one","two","three"] │
└───────────────────────┘
```
