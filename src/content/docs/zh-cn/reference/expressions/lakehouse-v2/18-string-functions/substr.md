---
title: SUBSTR (Lakehouse v2)
description: SUBSTR：从指定位置开始返回子字符串，长度可选。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/substr.md
---

从指定位置开始返回子字符串，长度可选。

## Analyze 语法

```python
func.substr(<str>, <pos>[, <len>])
```

## Analyze 示例

```python
func.substr('StarRocks', 5, 5)

┌─────────┐
│ 'Rocks'  │
└─────────┘
```

## SQL 语法

```sql
SUBSTR(<str>, <pos>[, <len>])
```

## SQL 示例

```sql
SELECT SUBSTR('StarRocks', 5, 5);

┌───────┐
│ Rocks  │
└───────┘
```
