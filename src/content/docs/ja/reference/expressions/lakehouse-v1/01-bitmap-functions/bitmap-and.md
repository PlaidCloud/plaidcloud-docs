---
title: BITMAP_AND (Lakehouse v1)
description: BITMAP_AND — 2つのビットマップに対してビット単位のAND演算を実行します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-and.md
---

2つのビットマップに対してビット単位のAND演算を実行します。

## Analyzeの構文

```python
func.bitmap_and( <bitmap1>, <bitmap2> )
```

## Analyzeの例

```python
func.bitmap_and(func.build_bitmap([1, 4, 5]), func.cast(build_bitmap([4, 5])), string)

┌────────────────────────────────────────────────────────────────────────────────────────┐
│ func.bitmap_and(func.build_bitmap([1, 4, 5]), func.cast(build_bitmap([4, 5])), string) │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 4,5                                                                                    │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

## SQLの構文

```sql
BITMAP_AND( <bitmap1>, <bitmap2> )
```

## SQLの例

```sql
SELECT BITMAP_AND(BUILD_BITMAP([1,4,5]), BUILD_BITMAP([4,5]))::String;

┌───────────────────────────────────────────────────────────────────┐
│ bitmap_and(build_bitmap([1, 4, 5]), build_bitmap([4, 5]))::string │
├───────────────────────────────────────────────────────────────────┤
│ 4,5                                                               │
└───────────────────────────────────────────────────────────────────┘
```
