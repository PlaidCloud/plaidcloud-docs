---
title: BITMAP_MAX (Lakehouse v1)
description: BITMAP_MAX — ビットマップ内の最大値を取得します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-max.md
---

ビットマップ内の最大値を取得します。

## Analyzeの構文

```python
func.bitmap_max( <bitmap> )
```

## Analyzeの例

```python
func.bitmap_max(func.build_bitmap([1, 4, 5]))

┌───────────────────────────────────────────────┐
│ func.bitmap_max(func.build_bitmap([1, 4, 5])) │
├───────────────────────────────────────────────┤
│                                             5 │
└───────────────────────────────────────────────┘
```

## SQLの構文

```sql
BITMAP_MAX( <bitmap> )
```

## SQLの例

```sql
SELECT BITMAP_MAX(BUILD_BITMAP([1,4,5]));

┌─────────────────────────────────────┐
│ bitmap_max(build_bitmap([1, 4, 5])) │
├─────────────────────────────────────┤
│                                   5 │
└─────────────────────────────────────┘
```
