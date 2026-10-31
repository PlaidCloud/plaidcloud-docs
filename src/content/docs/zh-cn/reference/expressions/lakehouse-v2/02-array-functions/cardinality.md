---
title: "CARDINALITY (Array, Lakehouse v2)"
description: CARDINALITY：返回数组中的元素个数，是 `ARRAY_LENGTH` 的别名。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/cardinality.md
---

返回数组中的元素个数，是 `ARRAY_LENGTH` 的别名。

## Analyze 语法

```python
func.cardinality([1, 2, 3])
```

## Analyze 示例

```python
func.cardinality([10, 20, 30])

┌───┐
│ 3 │
└───┘
```

## SQL 语法

```sql
CARDINALITY([1, 2, 3])
```

## SQL 示例

```sql
SELECT CARDINALITY([10, 20, 30]);

┌───┐
│ 3 │
└───┘
```
