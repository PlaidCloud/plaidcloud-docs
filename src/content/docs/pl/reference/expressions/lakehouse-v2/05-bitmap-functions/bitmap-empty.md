---
title: BITMAP_EMPTY (Lakehouse v2)
description: BITMAP_EMPTY — zwraca pustą bitmapę.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-empty.md
---

Zwraca pustą bitmapę.

## Składnia Analyze

```python
func.bitmap_empty()
```

## Przykłady Analyze

```python
func.bitmap_empty()

┌────────────────┐
│ (empty bitmap) │
└────────────────┘
```

## Składnia SQL

```sql
BITMAP_EMPTY()
```

## Przykłady SQL

```sql
SELECT BITMAP_COUNT(BITMAP_EMPTY());

┌───┐
│ 0 │
└───┘
```
