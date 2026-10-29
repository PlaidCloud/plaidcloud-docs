---
title: SUBDIVIDE_BITMAP (Lakehouse v2)
description: SUBDIVIDE_BITMAP — ビットマップを、指定したサイズの複数のサブビットマップに分割します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/subdivide-bitmap.md
---

ビットマップを、指定したサイズの複数のサブビットマップに分割します。

## Analyzeの構文

```python
func.subdivide_bitmap(<bitmap>, <size>)
```

## Analyzeの例

```python
func.subdivide_bitmap(get_column(table, 'bm'), 2)
```

## SQLの構文

```sql
SUBDIVIDE_BITMAP(<bitmap>, <size>)
```

## SQLの例

```sql
SELECT BITMAP_TO_STRING(bm) FROM TABLE(
  SUBDIVIDE_BITMAP(BITMAP_FROM_STRING('1,2,3,4'), 2));

┌──────┐
│ bm   │
├──────┤
│ 1,2  │
│ 3,4  │
└──────┘
```
