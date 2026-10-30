---
title: STRRIGHT (Lakehouse v2)
description: STRRIGHT：返回字符串最右侧的 N 个字符。是 `RIGHT` 的别名。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/strright.md
---

返回字符串最右侧的 N 个字符。是 `RIGHT` 的别名。

## Analyze 语法

```python
func.strright(<str>, <len>)
```

## Analyze 示例

```python
func.strright('StarRocks', 5)

┌─────────┐
│ 'Rocks'  │
└─────────┘
```

## SQL 语法

```sql
STRRIGHT(<str>, <len>)
```

## SQL 示例

```sql
SELECT STRRIGHT('StarRocks', 5);

┌───────┐
│ Rocks  │
└───────┘
```
