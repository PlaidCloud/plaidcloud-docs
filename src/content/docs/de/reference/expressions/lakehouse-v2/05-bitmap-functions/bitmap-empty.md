---
title: BITMAP_EMPTY (Lakehouse v2)
description: BITMAP_EMPTY – gibt eine leere Bitmap zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-empty.md
---

Gibt eine leere Bitmap zurück.

## Analyze-Syntax

```python
func.bitmap_empty()
```

## Analyze-Beispiele

```python
func.bitmap_empty()

┌────────────────┐
│ (empty bitmap) │
└────────────────┘
```

## SQL-Syntax

```sql
BITMAP_EMPTY()
```

## SQL-Beispiele

```sql
SELECT BITMAP_COUNT(BITMAP_EMPTY());

┌───┐
│ 0 │
└───┘
```
