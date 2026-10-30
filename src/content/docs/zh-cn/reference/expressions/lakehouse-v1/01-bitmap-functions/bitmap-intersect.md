---
title: BITMAP_INTERSECT (Lakehouse v1)
description: BITMAP_INTERSECT：通过执行逻辑 INTERSECT 运算，统计位图中值为 1 的位数。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-intersect.md
---

通过执行逻辑 INTERSECT 运算，统计位图中值为 1 的位数。

## Analyze 语法

```python
func.bitmap_intersect( <bitmap> )
```

## Analyze 示例

```python
func.bitmap_intersect(func.to_bitmap('1, 3, 5'))

┌──────────────────────────────────────────────────┐
│ func.bitmap_intersect(func.to_bitmap('1, 3, 5')) │
├──────────────────────────────────────────────────┤
│ 1,3,5                                            │
└──────────────────────────────────────────────────┘
```

## SQL 语法

```sql
BITMAP_INTERSECT( <bitmap> )
```

## SQL 示例

```sql
SELECT BITMAP_INTERSECT(TO_BITMAP('1, 3, 5'))::String;

┌────────────────────────────────────────────────┐
│ bitmap_intersect(to_bitmap('1, 3, 5'))::string │
├────────────────────────────────────────────────┤
│ 1,3,5                                          │
└────────────────────────────────────────────────┘
```
