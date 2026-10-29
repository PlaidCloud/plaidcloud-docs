---
title: BITMAP_HAS_ANY (Lakehouse v1)
description: BITMAP_HAS_ANY — 1番目のビットマップに、2番目のビットマップのビットと一致するビットが1つでもあるかどうかを確認します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-has-any.md
---

1番目のビットマップに、2番目のビットマップのビットと一致するビットが1つでもあるかどうかを確認します。

## Analyzeの構文

```python
func.bitmap_has_any( <bitmap1>, <bitmap2> )
```

## Analyzeの例

```python
func.bitmap_has_any(func.build_bitmap([1, 4, 5]), func.build_bitmap([1, 2]))

┌───────────────────────────────────────────────────────────────────────────────┐
│ func.bitmap_has_any(func.build_bitmap([1, 4, 5]), func.build_bitmap([1, 2]))  │
├───────────────────────────────────────────────────────────────────────────────┤
│ true                                                                          │
└───────────────────────────────────────────────────────────────────────────────┘
```

## SQLの構文

```sql
BITMAP_HAS_ANY( <bitmap1>, <bitmap2> )
```

## SQLの例

```sql
SELECT BITMAP_HAS_ANY(BUILD_BITMAP([1,4,5]), BUILD_BITMAP([1,2]));

┌───────────────────────────────────────────────────────────────┐
│ bitmap_has_any(build_bitmap([1, 4, 5]), build_bitmap([1, 2])) │
├───────────────────────────────────────────────────────────────┤
│ true                                                          │
└───────────────────────────────────────────────────────────────┘
```
