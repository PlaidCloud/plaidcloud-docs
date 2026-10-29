---
title: "REVERSE (Array, Lakehouse v2)"
description: REVERSE：返回元素顺序反转后的数组。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/reverse.md
---

返回元素顺序反转后的数组。

## Analyze 语法

```python
func.reverse([1, 2, 3])
```

## Analyze 示例

```python
func.reverse([1, 2, 3])

┌─────────┐
│ [3,2,1] │
└─────────┘
```

## SQL 语法

```sql
REVERSE([1, 2, 3])
```

## SQL 示例

```sql
SELECT ARRAY_REVERSE([1, 2, 3]);

┌─────────┐
│ [3,2,1] │
└─────────┘
```
