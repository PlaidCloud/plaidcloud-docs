---
title: BITMAP_OR_COUNT (Lakehouse v1)
description: BITMAP_OR_COUNT：通过执行逻辑 OR 运算，统计位图中值为 1 的位数。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-or-count.md
---

通过执行逻辑 OR 运算，统计位图中值为 1 的位数。

## Analyze 语法

```python
func.bitmap_or_count( <bitmap> )
```

## Analyze 示例

```python
func.bitmap_or_count(func.to_bitmap('1, 3, 5'))

┌─────────────────────────────────────────────────┐
│ func.bitmap_or_count(func.to_bitmap('1, 3, 5')) │
├─────────────────────────────────────────────────┤
│                                               3 │
└─────────────────────────────────────────────────┘
```

## SQL 语法

```sql
BITMAP_OR_COUNT( <bitmap> )
```

## SQL 示例

```sql
SELECT BITMAP_OR_COUNT(TO_BITMAP('1, 3, 5'));

┌───────────────────────────────────────┐
│ bitmap_or_count(to_bitmap('1, 3, 5')) │
├───────────────────────────────────────┤
│                                     3 │
└───────────────────────────────────────┘
```
