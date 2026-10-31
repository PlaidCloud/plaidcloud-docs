---
title: BITMAP_HASH64 (Lakehouse v2)
description: BITMAP_HASH64 — 値の 64 ビットハッシュを計算し、そのハッシュを含むビットマップを返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-hash64.md
---

値の 64 ビットハッシュを計算し、そのハッシュを含むビットマップを返します。

## Analyzeの構文

```python
func.bitmap_hash64(<value>)
```

## Analyzeの例

```python
func.bitmap_hash64('hello')

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQLの構文

```sql
BITMAP_HASH64(<value>)
```

## SQLの例

```sql
SELECT BITMAP_COUNT(BITMAP_HASH64('hello'));

┌───┐
│ 1 │
└───┘
```
