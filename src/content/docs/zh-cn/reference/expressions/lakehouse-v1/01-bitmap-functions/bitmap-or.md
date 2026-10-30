---
title: BITMAP_OR (Lakehouse v1)
description: BITMAP_OR：对两个位图执行按位 OR 运算。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-or.md
---

对两个位图执行按位 OR 运算。

## Analyze 语法

```python
func.bitmap_or( <bitmap1>, <bitmap2> )
```

## Analyze 示例

```python
func.bitmap_or(func.build_bitmap([1, 4, 5]), func.build_bitmap([6, 7]))

┌─────────────────────────────────────────────────────────────────────────┐
│ func.bitmap_or(func.build_bitmap([1, 4, 5]), func.build_bitmap([6, 7])) │
├─────────────────────────────────────────────────────────────────────────┤
│ 1,4,5,6,7                                                               │
└─────────────────────────────────────────────────────────────────────────┘
```

## SQL 语法

```sql
BITMAP_OR( <bitmap1>, <bitmap2> )
```

## SQL 示例

```sql
SELECT BITMAP_OR(BUILD_BITMAP([1,4,5]), BUILD_BITMAP([6,7]))::String;

┌──────────────────────────────────────────────────────────────────┐
│ bitmap_or(build_bitmap([1, 4, 5]), build_bitmap([6, 7]))::string │
├──────────────────────────────────────────────────────────────────┤
│ 1,4,5,6,7                                                        │
└──────────────────────────────────────────────────────────────────┘
```
