---
title: ARRAY_APPEND (Lakehouse v2)
description: ARRAY_APPEND：在数组末尾追加一个元素。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-append.md
---

在数组末尾追加一个元素。

## Analyze 语法

```python
func.array_append([1, 2, 3], 4)
```

## Analyze 示例

```python
func.array_append([1, 2, 3], 4)

┌───────────┐
│ [1,2,3,4] │
└───────────┘
```

## SQL 语法

```sql
ARRAY_APPEND([1, 2, 3], 4)
```

## SQL 示例

```sql
SELECT ARRAY_APPEND([1, 2, 3], 4);

┌───────────┐
│ [1,2,3,4] │
└───────────┘
```
