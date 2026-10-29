---
title: ARRAY_POSITION (Lakehouse v2)
description: ARRAY_POSITION：返回元素首次出现的位置（从 1 开始计数）。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-position.md
---

返回元素首次出现的位置（从 1 开始计数）。

## Analyze 语法

```python
func.array_position([10, 20, 30], 20)
```

## Analyze 示例

```python
func.array_position([10, 20, 30], 20)

┌───┐
│ 2 │
└───┘
```

## SQL 语法

```sql
ARRAY_POSITION([10, 20, 30], 20)
```

## SQL 示例

```sql
SELECT ARRAY_POSITION([10, 20, 30], 20);

┌───┐
│ 2 │
└───┘
```
