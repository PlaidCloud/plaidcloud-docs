---
title: REGEXP_EXTRACT_ALL (Lakehouse v2)
description: REGEXP_EXTRACT_ALL — 提取所有与正则表达式模式匹配的子字符串。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/14-pattern-matching-functions/regexp-extract-all.md
---

提取所有与正则表达式模式匹配的子字符串。

## Analyze 语法

```python
func.regexp_extract_all(<str>, <pattern>)
```

## Analyze 示例

```python
func.regexp_extract_all('a1b2c3', '\\d+')

┌───────────────┐
│ ['1','2','3']  │
└───────────────┘
```

## SQL 语法

```sql
REGEXP_EXTRACT_ALL(<str>, <pattern>)
```

## SQL 示例

```sql
SELECT REGEXP_EXTRACT_ALL('a1b2c3', '\\d+');

┌───────────────┐
│ ["1","2","3"]  │
└───────────────┘
```
