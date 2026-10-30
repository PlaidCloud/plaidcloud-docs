---
title: STRCMP (Lakehouse v2)
description: "在 PlaidCloud Lakehouse 中使用 STRCMP 字符串函数。按字典顺序比较两个字符串。相等时返回 0，str1 < str2 时返回 -1，str1 > str2 时返回 1。"
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/strcmp.md
---

按字典顺序比较两个字符串。相等时返回 0，str1 &lt; str2 时返回 -1，str1 > str2 时返回 1。

## Analyze 语法

```python
func.strcmp(<str1>, <str2>)
```

## Analyze 示例

```python
func.strcmp('abc', 'abd')

┌────┐
│ -1  │
└────┘
```

## SQL 语法

```sql
STRCMP(<str1>, <str2>)
```

## SQL 示例

```sql
SELECT STRCMP('abc', 'abd');

┌────┐
│ -1  │
└────┘
```
