---
title: BITMAP_HAS_ALL (Lakehouse v1)
description: BITMAP_HAS_ALL：检查第一个位图是否包含第二个位图中的所有位。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-has-all.md
---

检查第一个位图是否包含第二个位图中的所有位。

## Analyze 语法

```python
func.bitmap_has_all( <bitmap1>, <bitmap2> )
```

## Analyze 示例

```python
func.bitmap_has_all(build_bitmap([1, 4, 5]), build_bitmap([1, 2])) 

┌─────────────────────────────────────────────────────────────────────┐
│ func.bitmap_has_all(build_bitmap([1, 4, 5]), build_bitmap([1, 2]))  │
├─────────────────────────────────────────────────────────────────────┤
│ false                                                               │
└─────────────────────────────────────────────────────────────────────┘
```

## SQL 语法

```sql
BITMAP_HAS_ALL( <bitmap1>, <bitmap2> )
```

## SQL 示例

```sql
SELECT BITMAP_HAS_ALL(BUILD_BITMAP([1,4,5]), BUILD_BITMAP([1,2]));

┌───────────────────────────────────────────────────────────────┐
│ bitmap_has_all(build_bitmap([1, 4, 5]), build_bitmap([1, 2])) │
├───────────────────────────────────────────────────────────────┤
│ false                                                         │
└───────────────────────────────────────────────────────────────┘
```
