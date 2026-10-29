---
title: BITMAP_NOT_COUNT (Lakehouse v1)
description: BITMAP_NOT_COUNT — 論理NOT演算を実行して、ビットマップ内で0に設定されているビットの数を数えます。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-not-count.md
---

論理NOT演算を実行して、ビットマップ内で0に設定されているビットの数を数えます。

## Analyzeの構文

```python
func.bitmap_not_count( <bitmap> )
```

## Analyzeの例

```python
func.bitmap_not_count(func.to_bitmap('1, 3, 5'))

┌──────────────────────────────────────────────────┐
│ func.bitmap_not_count(func.to_bitmap('1, 3, 5')) │
├──────────────────────────────────────────────────┤
│                                                3 │
└──────────────────────────────────────────────────┘
```

## SQLの構文

```sql
BITMAP_NOT_COUNT( <bitmap> )
```

## SQLの例

```sql
SELECT BITMAP_NOT_COUNT(TO_BITMAP('1, 3, 5'));

┌────────────────────────────────────────┐
│ bitmap_not_count(to_bitmap('1, 3, 5')) │
├────────────────────────────────────────┤
│                                      3 │
└────────────────────────────────────────┘
```
