---
title: BITMAP_NOT (Lakehouse v1)
description: BITMAP_NOT：生成一个新位图，其元素来自第一个位图中不在第二个位图中的部分。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-not.md
---

生成一个新位图，其元素来自第一个位图中不在第二个位图中的部分。

## Analyze 语法

```python
func.bitmap_not( <bitmap1>, <bitmap2> )
```

## Analyze 示例

```python
func.bitmap_not(func.build_bitmap([1, 4, 5]), func.cast(func.build_bitmap([5, 6, 7])), Text)

┌───────────────────────────────────────────────────────────────────────────────────────────────┐
│ func.bitmap_not(func.build_bitmap([1, 4, 5]), func.cast(func.build_bitmap([5, 6, 7])), Text)  │
├───────────────────────────────────────────────────────────────────────────────────────────────┤
│ 1,4                                                                                           │
└───────────────────────────────────────────────────────────────────────────────────────────────┘
```

## SQL 语法

```sql
BITMAP_NOT( <bitmap1>, <bitmap2> )
```

## 别名

- [BITMAP_AND_NOT](../bitmap-and-not)

## SQL 示例

```sql
SELECT BITMAP_NOT(BUILD_BITMAP([1,4,5]), BUILD_BITMAP([5,6,7]))::String;

┌──────────────────────────────────────────────────────────────────────┐
│ bitmap_not(build_bitmap([1, 4, 5]), build_bitmap([5, 6, 7]))::string │
├──────────────────────────────────────────────────────────────────────┤
│ 1,4                                                                  │
└──────────────────────────────────────────────────────────────────────┘

SELECT BITMAP_AND_NOT(BUILD_BITMAP([1,4,5]), BUILD_BITMAP([5,6,7]))::String;

┌──────────────────────────────────────────────────────────────────────────┐
│ bitmap_and_not(build_bitmap([1, 4, 5]), build_bitmap([5, 6, 7]))::string │
├──────────────────────────────────────────────────────────────────────────┤
│ 1,4                                                                      │
└──────────────────────────────────────────────────────────────────────────┘
```
