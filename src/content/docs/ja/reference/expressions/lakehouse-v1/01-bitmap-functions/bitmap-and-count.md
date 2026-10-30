---
title: BITMAP_AND_COUNT (Lakehouse v1)
description: BITMAP_AND_COUNT — 論理AND演算を実行して、ビットマップ内で1に設定されているビットの数を数えます。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-and-count.md
---

論理AND演算を実行して、ビットマップ内で1に設定されているビットの数を数えます。

## Analyzeの構文

```python
func.bitmap_and_count( <bitmap> )
```

## Analyzeの例

```python
func.bitmap_and_count(to_bitmap('1, 3, 5'))

┌─────────────────────────────────────────────┐
│ func.bitmap_and_count(to_bitmap('1, 3, 5')) │
├─────────────────────────────────────────────┤
│                                           3 │
└─────────────────────────────────────────────┘
```

## SQLの構文

```sql
BITMAP_AND_COUNT( <bitmap> )
```

## SQLの例

```sql
SELECT BITMAP_AND_COUNT(TO_BITMAP('1, 3, 5'));

┌────────────────────────────────────────┐
│ bitmap_and_count(to_bitmap('1, 3, 5')) │
├────────────────────────────────────────┤
│                                      3 │
└────────────────────────────────────────┘
```
