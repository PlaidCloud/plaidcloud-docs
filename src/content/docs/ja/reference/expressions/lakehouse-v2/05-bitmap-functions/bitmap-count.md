---
title: BITMAP_COUNT (Lakehouse v2)
description: BITMAP_COUNT — ビットマップ内で設定されているビットの数を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-count.md
---

ビットマップ内で設定されているビットの数を返します。

## Analyzeの構文

```python
func.bitmap_count(<bitmap>)
```

## Analyzeの例

```python
func.bitmap_count(get_column(table, 'bm'))

┌───┐
│ 3 │
└───┘
```

## SQLの構文

```sql
BITMAP_COUNT(<bitmap>)
```

## SQLの例

```sql
SELECT BITMAP_COUNT(BITMAP_FROM_STRING('1,2,3'));

┌───┐
│ 3 │
└───┘
```
