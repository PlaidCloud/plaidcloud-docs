---
title: TO_BITMAP (Lakehouse v2)
description: TO_BITMAP — konwertuje wartość całkowitą na bitmapę zawierającą tę jedną wartość.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/to-bitmap.md
---

Konwertuje wartość całkowitą na bitmapę zawierającą tę jedną wartość.

## Składnia Analyze

```python
func.to_bitmap(<value>)
```

## Przykłady Analyze

```python
func.to_bitmap(42)

┌──────────┐
│ (bitmap) │
└──────────┘
```

## Składnia SQL

```sql
TO_BITMAP(<value>)
```

## Przykłady SQL

```sql
SELECT BITMAP_TO_STRING(TO_BITMAP(42));

┌────┐
│ 42 │
└────┘
```
