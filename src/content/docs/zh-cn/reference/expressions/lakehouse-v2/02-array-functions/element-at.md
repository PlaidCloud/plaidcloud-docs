---
title: "ELEMENT_AT (Array, Lakehouse v2)"
description: ELEMENT_AT：返回数组中指定位置的元素（从 1 开始计数）。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/element-at.md
---

返回数组中指定位置的元素（从 1 开始计数）。

## Analyze 语法

```python
func.element_at([10, 20, 30], 2)
```

## Analyze 示例

```python
func.element_at([10, 20, 30], 2)

┌────┐
│ 20 │
└────┘
```

## SQL 语法

```sql
ELEMENT_AT([10, 20, 30], 2)
```

## SQL 示例

```sql
SELECT ELEMENT_AT([10, 20, 30], 2);

┌────┐
│ 20 │
└────┘
```
