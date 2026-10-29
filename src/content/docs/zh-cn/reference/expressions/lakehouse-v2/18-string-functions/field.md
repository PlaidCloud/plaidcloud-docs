---
title: FIELD (Lakehouse v2)
description: FIELD：返回某个值在参数列表中的索引位置。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/field.md
---

返回某个值在参数列表中的索引位置。

## Analyze 语法

```python
func.field(<str>, <val1>, <val2>[, ...])
```

## Analyze 示例

```python
func.field('b', 'a', 'b', 'c')

┌───┐
│ 2  │
└───┘
```

## SQL 语法

```sql
FIELD(<str>, <val1>, <val2>[, ...])
```

## SQL 示例

```sql
SELECT FIELD('b', 'a', 'b', 'c');

┌───┐
│ 2  │
└───┘
```
