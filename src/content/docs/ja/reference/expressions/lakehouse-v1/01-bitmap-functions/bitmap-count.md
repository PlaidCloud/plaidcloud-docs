---
title: BITMAP_COUNT (Lakehouse v1)
description: BITMAP_COUNT — ビットマップ内で1に設定されているビットの数を数えます。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-count.md
---

ビットマップ内で1に設定されているビットの数を数えます。

## Analyzeの構文

```python
func.bitmap_count( <bitmap> )
```

## Analyzeの例

```python
func.bitmap_count(build_bitmap([1, 4, 5]))

┌────────────────────────────────────────────┐
│ func.bitmap_count(build_bitmap([1, 4, 5])) │
├────────────────────────────────────────────┤
│                                          3 │
└────────────────────────────────────────────┘
```

## SQLの構文

```sql
BITMAP_COUNT( <bitmap> )
```

## エイリアス

- [BITMAP_CARDINALITY](../bitmap-cardinality)

## SQLの例

```sql
SELECT BITMAP_COUNT(BUILD_BITMAP([1,4,5])), BITMAP_CARDINALITY(BUILD_BITMAP([1,4,5]));

┌─────────────────────────────────────────────────────────────────────────────────────┐
│ bitmap_count(build_bitmap([1, 4, 5])) │ bitmap_cardinality(build_bitmap([1, 4, 5])) │
├───────────────────────────────────────┼─────────────────────────────────────────────┤
│                                     3 │                                           3 │
└─────────────────────────────────────────────────────────────────────────────────────┘
```
