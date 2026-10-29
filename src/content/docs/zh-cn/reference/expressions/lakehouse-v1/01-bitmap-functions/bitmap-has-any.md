---
title: BITMAP_HAS_ANY (Lakehouse v1)
description: BITMAP_HAS_ANY：检查第一个位图中是否有任意位与第二个位图中的位匹配。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-has-any.md
---

检查第一个位图中是否有任意位与第二个位图中的位匹配。

## Analyze 语法

```python
func.bitmap_has_any( <bitmap1>, <bitmap2> )
```

## Analyze 示例

```python
func.bitmap_has_any(func.build_bitmap([1, 4, 5]), func.build_bitmap([1, 2]))

┌───────────────────────────────────────────────────────────────────────────────┐
│ func.bitmap_has_any(func.build_bitmap([1, 4, 5]), func.build_bitmap([1, 2]))  │
├───────────────────────────────────────────────────────────────────────────────┤
│ true                                                                          │
└───────────────────────────────────────────────────────────────────────────────┘
```

## SQL 语法

```sql
BITMAP_HAS_ANY( <bitmap1>, <bitmap2> )
```

## SQL 示例

```sql
SELECT BITMAP_HAS_ANY(BUILD_BITMAP([1,4,5]), BUILD_BITMAP([1,2]));

┌───────────────────────────────────────────────────────────────┐
│ bitmap_has_any(build_bitmap([1, 4, 5]), build_bitmap([1, 2])) │
├───────────────────────────────────────────────────────────────┤
│ true                                                          │
└───────────────────────────────────────────────────────────────┘
```
