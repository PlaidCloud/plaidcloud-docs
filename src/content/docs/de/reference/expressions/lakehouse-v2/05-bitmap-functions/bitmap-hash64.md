---
title: BITMAP_HASH64 (Lakehouse v2)
description: BITMAP_HASH64 – berechnet einen 64-Bit-Hash eines Werts und gibt eine Bitmap zurück, die diesen Hash enthält.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-hash64.md
---

Berechnet einen 64-Bit-Hash eines Werts und gibt eine Bitmap zurück, die diesen Hash enthält.

## Analyze-Syntax

```python
func.bitmap_hash64(<value>)
```

## Analyze-Beispiele

```python
func.bitmap_hash64('hello')

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQL-Syntax

```sql
BITMAP_HASH64(<value>)
```

## SQL-Beispiele

```sql
SELECT BITMAP_COUNT(BITMAP_HASH64('hello'));

┌───┐
│ 1 │
└───┘
```
