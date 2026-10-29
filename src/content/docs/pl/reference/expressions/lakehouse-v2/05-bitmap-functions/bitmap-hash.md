---
title: BITMAP_HASH (Lakehouse v2)
description: BITMAP_HASH — oblicza 32-bitowy skrót wartości i zwraca bitmapę zawierającą ten skrót.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-hash.md
---

Oblicza 32-bitowy skrót wartości i zwraca bitmapę zawierającą ten skrót.

## Składnia Analyze

```python
func.bitmap_hash(<value>)
```

## Przykłady Analyze

```python
func.bitmap_hash('hello')

┌──────────┐
│ (bitmap) │
└──────────┘
```

## Składnia SQL

```sql
BITMAP_HASH(<value>)
```

## Przykłady SQL

```sql
SELECT BITMAP_COUNT(BITMAP_HASH('hello'));

┌───┐
│ 1 │
└───┘
```
