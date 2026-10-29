---
title: BITMAP_SUBSET_LIMIT (Lakehouse v1)
description: BITMAP_SUBSET_LIMIT：生成源位图的子位图，从起始值开始取一个范围，并限制大小。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-subset-limit.md
---

生成源位图的子位图，从起始值开始取一个范围，并限制大小。

## Analyze 语法

```python
func.bitmap_subset_limit( <bitmap>, <start>, <limit> )
```

## Analyze 示例

```python
func.bitmap_subset_limit(func.build_bitmap([1, 4, 5]), 2, 2)

┌──────────────────────────────────────────────────────────────┐
│ func.bitmap_subset_limit(func.build_bitmap([1, 4, 5]), 2, 2) │
├──────────────────────────────────────────────────────────────┤
│ 4,5                                                          │
└──────────────────────────────────────────────────────────────┘
```

## SQL 语法

```sql
BITMAP_SUBSET_LIMIT( <bitmap>, <start>, <limit> )
```

## SQL 示例

```sql
SELECT BITMAP_SUBSET_LIMIT(BUILD_BITMAP([1,4,5]), 2, 2)::String;

┌────────────────────────────────────────────────────────────┐
│ bitmap_subset_limit(build_bitmap([1, 4, 5]), 2, 2)::string │
├────────────────────────────────────────────────────────────┤
│ 4,5                                                        │
└────────────────────────────────────────────────────────────┘
```
