---
title: ALL_MATCH (Lakehouse v2)
description: ALL_MATCH：如果数组中的所有元素都满足给定谓词，则返回 TRUE。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/all-match.md
---

如果数组中的所有元素都满足给定谓词，则返回 TRUE。

## Analyze 语法

```python
func.all_match(get_column(table, 'arr'), lambda x: x > 0)
```

## Analyze 示例

```python
func.all_match([1, 2, 3], lambda x: x > 0)

┌───┐
│ 1 │
└───┘
```

## SQL 语法

```sql
ALL_MATCH(<arr>, lambda x: x > 0)
```

## SQL 示例

```sql
SELECT ALL_MATCH([1, 2, 3], x -> x > 0);

┌───┐
│ 1 │
└───┘
```
