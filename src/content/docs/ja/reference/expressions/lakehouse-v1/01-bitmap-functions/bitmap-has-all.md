---
title: BITMAP_HAS_ALL (Lakehouse v1)
description: BITMAP_HAS_ALL — 1番目のビットマップに、2番目のビットマップのすべてのビットが含まれているかどうかを確認します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-has-all.md
---

1番目のビットマップに、2番目のビットマップのすべてのビットが含まれているかどうかを確認します。

## Analyzeの構文

```python
func.bitmap_has_all( <bitmap1>, <bitmap2> )
```

## Analyzeの例

```python
func.bitmap_has_all(build_bitmap([1, 4, 5]), build_bitmap([1, 2])) 

┌─────────────────────────────────────────────────────────────────────┐
│ func.bitmap_has_all(build_bitmap([1, 4, 5]), build_bitmap([1, 2]))  │
├─────────────────────────────────────────────────────────────────────┤
│ false                                                               │
└─────────────────────────────────────────────────────────────────────┘
```

## SQLの構文

```sql
BITMAP_HAS_ALL( <bitmap1>, <bitmap2> )
```

## SQLの例

```sql
SELECT BITMAP_HAS_ALL(BUILD_BITMAP([1,4,5]), BUILD_BITMAP([1,2]));

┌───────────────────────────────────────────────────────────────┐
│ bitmap_has_all(build_bitmap([1, 4, 5]), build_bitmap([1, 2])) │
├───────────────────────────────────────────────────────────────┤
│ false                                                         │
└───────────────────────────────────────────────────────────────┘
```
