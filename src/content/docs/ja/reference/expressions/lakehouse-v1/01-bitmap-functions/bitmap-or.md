---
title: BITMAP_OR (Lakehouse v1)
description: BITMAP_OR — 2つのビットマップに対してビット単位のOR演算を実行します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-or.md
---

2つのビットマップに対してビット単位のOR演算を実行します。

## Analyzeの構文

```python
func.bitmap_or( <bitmap1>, <bitmap2> )
```

## Analyzeの例

```python
func.bitmap_or(func.build_bitmap([1, 4, 5]), func.build_bitmap([6, 7]))

┌─────────────────────────────────────────────────────────────────────────┐
│ func.bitmap_or(func.build_bitmap([1, 4, 5]), func.build_bitmap([6, 7])) │
├─────────────────────────────────────────────────────────────────────────┤
│ 1,4,5,6,7                                                               │
└─────────────────────────────────────────────────────────────────────────┘
```

## SQLの構文

```sql
BITMAP_OR( <bitmap1>, <bitmap2> )
```

## SQLの例

```sql
SELECT BITMAP_OR(BUILD_BITMAP([1,4,5]), BUILD_BITMAP([6,7]))::String;

┌──────────────────────────────────────────────────────────────────┐
│ bitmap_or(build_bitmap([1, 4, 5]), build_bitmap([6, 7]))::string │
├──────────────────────────────────────────────────────────────────┤
│ 1,4,5,6,7                                                        │
└──────────────────────────────────────────────────────────────────┘
```
