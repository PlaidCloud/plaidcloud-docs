---
title: ARRAY_CONTAINS (Lakehouse v2)
description: ARRAY_CONTAINS：检查数组是否包含指定元素。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-contains.md
---

检查数组是否包含指定元素。

## Analyze 语法

```python
func.array_contains([1, 2, 3], 2)
```

## Analyze 示例

```python
func.array_contains([1, 2, 3], 2)

┌───┐
│ 1 │
└───┘
```

## SQL 语法

```sql
ARRAY_CONTAINS([1, 2, 3], 2)
```

## SQL 示例

```sql
SELECT ARRAY_CONTAINS([1, 2, 3], 2);

┌───┐
│ 1 │
└───┘
```
