---
title: BITMAP_MIN (Lakehouse v2)
description: BITMAP_MIN — ビットマップ内の最小値を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-min.md
---

ビットマップ内の最小値を返します。

## Analyzeの構文

```python
func.bitmap_min(<bitmap>)
```

## Analyzeの例

```python
func.bitmap_min(get_column(table, 'bm'))

┌───┐
│ 1 │
└───┘
```

## SQLの構文

```sql
BITMAP_MIN(<bitmap>)
```

## SQLの例

```sql
SELECT BITMAP_MIN(BITMAP_FROM_STRING('1,50,100'));

┌───┐
│ 1 │
└───┘
```
