---
title: BITMAP_HASH64 (Lakehouse v2)
description: BITMAP_HASH64 — oblicza 64-bitowy skrót wartości i zwraca bitmapę zawierającą ten skrót.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-hash64.md
---

Oblicza 64-bitowy skrót wartości i zwraca bitmapę zawierającą ten skrót.

## Składnia Analyze

```python
func.bitmap_hash64(<value>)
```

## Przykłady Analyze

```python
func.bitmap_hash64('hello')

┌──────────┐
│ (bitmap) │
└──────────┘
```

## Składnia SQL

```sql
BITMAP_HASH64(<value>)
```

## Przykłady SQL

```sql
SELECT BITMAP_COUNT(BITMAP_HASH64('hello'));

┌───┐
│ 1 │
└───┘
```
