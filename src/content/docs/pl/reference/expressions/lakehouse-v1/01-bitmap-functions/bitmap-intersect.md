---
title: BITMAP_INTERSECT (Lakehouse v1)
description: BITMAP_INTERSECT — zlicza bity ustawione na 1 w mapie bitowej, wykonując operację logiczną INTERSECT.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-intersect.md
---

Zlicza bity ustawione na 1 w mapie bitowej, wykonując operację logiczną INTERSECT.

## Składnia Analyze

```python
func.bitmap_intersect( <bitmap> )
```

## Przykłady Analyze

```python
func.bitmap_intersect(func.to_bitmap('1, 3, 5'))

┌──────────────────────────────────────────────────┐
│ func.bitmap_intersect(func.to_bitmap('1, 3, 5')) │
├──────────────────────────────────────────────────┤
│ 1,3,5                                            │
└──────────────────────────────────────────────────┘
```

## Składnia SQL

```sql
BITMAP_INTERSECT( <bitmap> )
```

## Przykłady SQL

```sql
SELECT BITMAP_INTERSECT(TO_BITMAP('1, 3, 5'))::String;

┌────────────────────────────────────────────────┐
│ bitmap_intersect(to_bitmap('1, 3, 5'))::string │
├────────────────────────────────────────────────┤
│ 1,3,5                                          │
└────────────────────────────────────────────────┘
```
