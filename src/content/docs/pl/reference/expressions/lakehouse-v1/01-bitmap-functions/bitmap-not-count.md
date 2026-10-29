---
title: BITMAP_NOT_COUNT (Lakehouse v1)
description: BITMAP_NOT_COUNT — zlicza bity ustawione na 0 w mapie bitowej, wykonując operację logiczną NOT.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-not-count.md
---

Zlicza bity ustawione na 0 w mapie bitowej, wykonując operację logiczną NOT.

## Składnia Analyze

```python
func.bitmap_not_count( <bitmap> )
```

## Przykłady Analyze

```python
func.bitmap_not_count(func.to_bitmap('1, 3, 5'))

┌──────────────────────────────────────────────────┐
│ func.bitmap_not_count(func.to_bitmap('1, 3, 5')) │
├──────────────────────────────────────────────────┤
│                                                3 │
└──────────────────────────────────────────────────┘
```

## Składnia SQL

```sql
BITMAP_NOT_COUNT( <bitmap> )
```

## Przykłady SQL

```sql
SELECT BITMAP_NOT_COUNT(TO_BITMAP('1, 3, 5'));

┌────────────────────────────────────────┐
│ bitmap_not_count(to_bitmap('1, 3, 5')) │
├────────────────────────────────────────┤
│                                      3 │
└────────────────────────────────────────┘
```
