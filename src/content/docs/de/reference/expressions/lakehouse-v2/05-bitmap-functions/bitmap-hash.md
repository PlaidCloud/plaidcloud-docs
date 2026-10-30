---
title: BITMAP_HASH (Lakehouse v2)
description: BITMAP_HASH – berechnet einen 32-Bit-Hash eines Werts und gibt eine Bitmap zurück, die diesen Hash enthält.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-hash.md
---

Berechnet einen 32-Bit-Hash eines Werts und gibt eine Bitmap zurück, die diesen Hash enthält.

## Analyze-Syntax

```python
func.bitmap_hash(<value>)
```

## Analyze-Beispiele

```python
func.bitmap_hash('hello')

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQL-Syntax

```sql
BITMAP_HASH(<value>)
```

## SQL-Beispiele

```sql
SELECT BITMAP_COUNT(BITMAP_HASH('hello'));

┌───┐
│ 1 │
└───┘
```
