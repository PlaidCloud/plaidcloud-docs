---
title: RIGHT (Lakehouse v2)
description: RIGHT：返回字符串最右侧的 N 个字符。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/right.md
---

返回字符串最右侧的 N 个字符。

## Analyze 语法

```python
func.right(<str>, <len>)
```

## Analyze 示例

```python
func.right('StarRocks', 5)

┌─────────┐
│ 'Rocks'  │
└─────────┘
```

## SQL 语法

```sql
RIGHT(<str>, <len>)
```

## SQL 示例

```sql
SELECT RIGHT('StarRocks', 5);

┌───────┐
│ Rocks  │
└───────┘
```
