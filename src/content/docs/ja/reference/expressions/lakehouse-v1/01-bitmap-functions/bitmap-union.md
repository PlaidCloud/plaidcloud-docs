---
title: BITMAP_UNION (Lakehouse v1)
description: BITMAP_UNION — 論理UNION演算を実行して、ビットマップ内で1に設定されているビットの数を数えます。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-union.md
---

論理UNION演算を実行して、ビットマップ内で1に設定されているビットの数を数えます。

## Analyzeの構文

```python
func.bitmap_union( <bitmap> )
```

## Analyzeの例

```python
func.bitmap_union(func.to_bitmap('1, 3, 5'))

┌──────────────────────────────────────────────┐
│ func.bitmap_union(func.to_bitmap('1, 3, 5')) │
├──────────────────────────────────────────────┤
│ 1,3,5                                        │
└──────────────────────────────────────────────┘
```

## SQLの構文

```sql
BITMAP_UNION( <bitmap> )
```

## SQLの例

```sql
SELECT BITMAP_UNION(TO_BITMAP('1, 3, 5'))::String;

┌────────────────────────────────────────────┐
│ bitmap_union(to_bitmap('1, 3, 5'))::string │
├────────────────────────────────────────────┤
│ 1,3,5                                      │
└────────────────────────────────────────────┘
```
