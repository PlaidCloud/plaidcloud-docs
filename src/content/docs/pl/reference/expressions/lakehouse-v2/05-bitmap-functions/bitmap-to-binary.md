---
title: BITMAP_TO_BINARY (Lakehouse v2)
description: BITMAP_TO_BINARY — konwertuje bitmapę na wartość binarną.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-to-binary.md
---

Konwertuje bitmapę na wartość binarną.

## Składnia Analyze

```python
func.bitmap_to_binary(<bitmap>)
```

## Przykłady Analyze

```python
func.bitmap_to_binary(get_column(table, 'bm'))

┌──────────┐
│ (binary) │
└──────────┘
```

## Składnia SQL

```sql
BITMAP_TO_BINARY(<bitmap>)
```

## Przykłady SQL

```sql
SELECT HEX(BITMAP_TO_BINARY(BITMAP_FROM_STRING('1,2,3')));

┌──────────────┐
│ (hex string) │
└──────────────┘
```
