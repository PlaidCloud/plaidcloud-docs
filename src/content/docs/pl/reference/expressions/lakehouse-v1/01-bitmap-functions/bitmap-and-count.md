---
title: BITMAP_AND_COUNT (Lakehouse v1)
description: BITMAP_AND_COUNT — zlicza bity ustawione na 1 w mapie bitowej, wykonując operację logiczną AND.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-and-count.md
---

Zlicza bity ustawione na 1 w mapie bitowej, wykonując operację logiczną AND.

## Składnia Analyze

```python
func.bitmap_and_count( <bitmap> )
```

## Przykłady Analyze

```python
func.bitmap_and_count(to_bitmap('1, 3, 5'))

┌─────────────────────────────────────────────┐
│ func.bitmap_and_count(to_bitmap('1, 3, 5')) │
├─────────────────────────────────────────────┤
│                                           3 │
└─────────────────────────────────────────────┘
```

## Składnia SQL

```sql
BITMAP_AND_COUNT( <bitmap> )
```

## Przykłady SQL

```sql
SELECT BITMAP_AND_COUNT(TO_BITMAP('1, 3, 5'));

┌────────────────────────────────────────┐
│ bitmap_and_count(to_bitmap('1, 3, 5')) │
├────────────────────────────────────────┤
│                                      3 │
└────────────────────────────────────────┘
```
