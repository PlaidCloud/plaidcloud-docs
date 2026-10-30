---
title: BITMAP_INTERSECT (Lakehouse v1)
description: BITMAP_INTERSECT — 論理INTERSECT演算を実行して、ビットマップ内で1に設定されているビットの数を数えます。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-intersect.md
---

論理INTERSECT演算を実行して、ビットマップ内で1に設定されているビットの数を数えます。

## Analyzeの構文

```python
func.bitmap_intersect( <bitmap> )
```

## Analyzeの例

```python
func.bitmap_intersect(func.to_bitmap('1, 3, 5'))

┌──────────────────────────────────────────────────┐
│ func.bitmap_intersect(func.to_bitmap('1, 3, 5')) │
├──────────────────────────────────────────────────┤
│ 1,3,5                                            │
└──────────────────────────────────────────────────┘
```

## SQLの構文

```sql
BITMAP_INTERSECT( <bitmap> )
```

## SQLの例

```sql
SELECT BITMAP_INTERSECT(TO_BITMAP('1, 3, 5'))::String;

┌────────────────────────────────────────────────┐
│ bitmap_intersect(to_bitmap('1, 3, 5'))::string │
├────────────────────────────────────────────────┤
│ 1,3,5                                          │
└────────────────────────────────────────────────┘
```
