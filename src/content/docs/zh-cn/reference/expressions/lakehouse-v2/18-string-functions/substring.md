---
title: SUBSTRING (Lakehouse v2)
description: SUBSTRING：从指定位置开始返回子字符串。是 `SUBSTR` 的别名。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/substring.md
---

从指定位置开始返回子字符串。是 `SUBSTR` 的别名。

## Analyze 语法

```python
func.substring(<str>, <pos>[, <len>])
```

## Analyze 示例

```python
func.substring('StarRocks', 1, 4)

┌────────┐
│ 'Star'  │
└────────┘
```

## SQL 语法

```sql
SUBSTRING(<str>, <pos>[, <len>])
```

## SQL 示例

```sql
SELECT SUBSTRING('StarRocks', 1, 4);

┌──────┐
│ Star  │
└──────┘
```
