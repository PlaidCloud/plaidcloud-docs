---
title: BITMAP_UNION (Lakehouse v1)
description: BITMAP_UNION — zlicza bity ustawione na 1 w mapie bitowej, wykonując operację logiczną UNION.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-union.md
---

Zlicza bity ustawione na 1 w mapie bitowej, wykonując operację logiczną UNION.

## Składnia Analyze

```python
func.bitmap_union( <bitmap> )
```

## Przykłady Analyze

```python
func.bitmap_union(func.to_bitmap('1, 3, 5'))

┌──────────────────────────────────────────────┐
│ func.bitmap_union(func.to_bitmap('1, 3, 5')) │
├──────────────────────────────────────────────┤
│ 1,3,5                                        │
└──────────────────────────────────────────────┘
```

## Składnia SQL

```sql
BITMAP_UNION( <bitmap> )
```

## Przykłady SQL

```sql
SELECT BITMAP_UNION(TO_BITMAP('1, 3, 5'))::String;

┌────────────────────────────────────────────┐
│ bitmap_union(to_bitmap('1, 3, 5'))::string │
├────────────────────────────────────────────┤
│ 1,3,5                                      │
└────────────────────────────────────────────┘
```
