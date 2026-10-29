---
title: BITMAP_FROM_BINARY (Lakehouse v2)
description: BITMAP_FROM_BINARY — バイナリ値をビットマップに変換します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-from-binary.md
---

バイナリ値をビットマップに変換します。

## Analyzeの構文

```python
func.bitmap_from_binary(<binary>)
```

## Analyzeの例

```python
func.bitmap_from_binary(get_column(table, 'bin_col'))

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQLの構文

```sql
BITMAP_FROM_BINARY(<binary>)
```

## SQLの例

```sql
SELECT BITMAP_COUNT(BITMAP_FROM_BINARY(bm_binary)) FROM data;

┌───┐
│ 5 │
└───┘
```
