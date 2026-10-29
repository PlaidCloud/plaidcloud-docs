---
title: SPLIT (Lakehouse v2)
description: SPLIT：按分隔符拆分字符串，并返回数组。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/split.md
---

按分隔符拆分字符串，并返回数组。

## Analyze 语法

```python
func.split(<str>, <delimiter>)
```

## Analyze 示例

```python
func.split('a,b,c', ',')

┌───────────────┐
│ ['a','b','c']  │
└───────────────┘
```

## SQL 语法

```sql
SPLIT(<str>, <delimiter>)
```

## SQL 示例

```sql
SELECT SPLIT('a,b,c', ',');

┌───────────────┐
│ ["a","b","c"]  │
└───────────────┘
```
