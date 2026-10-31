---
title: BITMAP_XOR (Lakehouse v1)
description: BITMAP_XOR：对两个位图执行按位 XOR（异或）运算。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-xor.md
---

对两个位图执行按位 XOR（异或）运算。

## Analyze 语法

```python
func.bitmap_xor( <bitmap1>, <bitmap2> )
```

## Analyze 示例

```python
func.bitmap_xor(func.build_bitmap([1, 4, 5]), func.build_bitmap([5, 6, 7]))

┌─────────────────────────────────────────────────────────────────────────────┐
│ func.bitmap_xor(func.build_bitmap([1, 4, 5]), func.build_bitmap([5, 6, 7])) │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1,4,6,7                                                                     │
└─────────────────────────────────────────────────────────────────────────────┘
```

## SQL 语法

```sql
BITMAP_XOR( <bitmap1>, <bitmap2> )
```

## SQL 示例

```sql
SELECT BITMAP_XOR(BUILD_BITMAP([1,4,5]), BUILD_BITMAP([5,6,7]))::String;

┌──────────────────────────────────────────────────────────────────────┐
│ bitmap_xor(build_bitmap([1, 4, 5]), build_bitmap([5, 6, 7]))::string │
├──────────────────────────────────────────────────────────────────────┤
│ 1,4,6,7                                                              │
└──────────────────────────────────────────────────────────────────────┘
```
