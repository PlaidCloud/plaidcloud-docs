---
title: BITMAP_OR_COUNT (Lakehouse v1)
description: BITMAP_OR_COUNT — zlicza bity ustawione na 1 w mapie bitowej, wykonując operację logiczną OR.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-or-count.md
---

Zlicza bity ustawione na 1 w mapie bitowej, wykonując operację logiczną OR.

## Składnia Analyze

```python
func.bitmap_or_count( <bitmap> )
```

## Przykłady Analyze

```python
func.bitmap_or_count(func.to_bitmap('1, 3, 5'))

┌─────────────────────────────────────────────────┐
│ func.bitmap_or_count(func.to_bitmap('1, 3, 5')) │
├─────────────────────────────────────────────────┤
│                                               3 │
└─────────────────────────────────────────────────┘
```

## Składnia SQL

```sql
BITMAP_OR_COUNT( <bitmap> )
```

## Przykłady SQL

```sql
SELECT BITMAP_OR_COUNT(TO_BITMAP('1, 3, 5'));

┌───────────────────────────────────────┐
│ bitmap_or_count(to_bitmap('1, 3, 5')) │
├───────────────────────────────────────┤
│                                     3 │
└───────────────────────────────────────┘
```
