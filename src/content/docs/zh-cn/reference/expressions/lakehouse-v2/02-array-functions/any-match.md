---
title: ANY_MATCH (Lakehouse v2)
description: ANY_MATCH：如果数组中有任意元素满足给定谓词，则返回 TRUE。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/any-match.md
---

如果数组中有任意元素满足给定谓词，则返回 TRUE。

## Analyze 语法

```python
func.any_match(get_column(table, 'arr'), lambda x: x > 5)
```

## Analyze 示例

```python
func.any_match([1, 2, 8], lambda x: x > 5)

┌───┐
│ 1 │
└───┘
```

## SQL 语法

```sql
ANY_MATCH(<arr>, lambda x: x > 5)
```

## SQL 示例

```sql
SELECT ANY_MATCH([1, 2, 8], x -> x > 5);

┌───┐
│ 1 │
└───┘
```
