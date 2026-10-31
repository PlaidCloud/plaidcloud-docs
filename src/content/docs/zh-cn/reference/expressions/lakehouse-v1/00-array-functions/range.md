---
title: RANGE (Lakehouse v1)
description: RANGE：返回由 [start, end) 区间生成的数组。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/range.md
---

返回由 [start, end) 区间生成的数组。

## Analyze 语法

```python
func.range( <start>, <end> )
```

## Analyze 示例

```python
func.range(1, 5)

┌────────────────────┐
│  func.range(1, 5)  │
├────────────────────┤
│ [1,2,3,4]          │
└────────────────────┘
```

## SQL 语法

```sql
RANGE( <start>, <end> )
```

## SQL 示例

```sql
SELECT RANGE(1, 5);

┌───────────────┐
│  range(1, 5)  │
├───────────────┤
│ [1,2,3,4]     │
└───────────────┘
```
