---
title: BITMAP_MAX (Lakehouse v2)
description: BITMAP_MAX — ビットマップ内の最大値を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-max.md
---

ビットマップ内の最大値を返します。

## Analyzeの構文

```python
func.bitmap_max(<bitmap>)
```

## Analyzeの例

```python
func.bitmap_max(get_column(table, 'bm'))

┌─────┐
│ 100 │
└─────┘
```

## SQLの構文

```sql
BITMAP_MAX(<bitmap>)
```

## SQLの例

```sql
SELECT BITMAP_MAX(BITMAP_FROM_STRING('1,50,100'));

┌─────┐
│ 100 │
└─────┘
```
