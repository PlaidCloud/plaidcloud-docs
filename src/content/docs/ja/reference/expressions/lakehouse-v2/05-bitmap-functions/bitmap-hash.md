---
title: BITMAP_HASH (Lakehouse v2)
description: BITMAP_HASH — 値の 32 ビットハッシュを計算し、そのハッシュを含むビットマップを返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-hash.md
---

値の 32 ビットハッシュを計算し、そのハッシュを含むビットマップを返します。

## Analyzeの構文

```python
func.bitmap_hash(<value>)
```

## Analyzeの例

```python
func.bitmap_hash('hello')

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQLの構文

```sql
BITMAP_HASH(<value>)
```

## SQLの例

```sql
SELECT BITMAP_COUNT(BITMAP_HASH('hello'));

┌───┐
│ 1 │
└───┘
```
