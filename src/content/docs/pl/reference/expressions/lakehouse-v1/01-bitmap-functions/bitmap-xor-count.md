---
title: BITMAP_XOR_COUNT (Lakehouse v1)
description: BITMAP_XOR_COUNT — zlicza bity ustawione na 1 w mapie bitowej, wykonując operację logiczną XOR.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-xor-count.md
---

Zlicza bity ustawione na 1 w mapie bitowej, wykonując operację logiczną XOR (alternatywa wykluczająca).

## Składnia Analyze

```python
func.bitmap_xor_count( <bitmap> )
```

## Przykłady Analyze

```python
func.bitmap_xor_count(func.to_bitmap('1, 3, 5'))

┌──────────────────────────────────────────────────┐
│ func.bitmap_xor_count(func.to_bitmap('1, 3, 5')) │
├──────────────────────────────────────────────────┤
│                                                3 │
└──────────────────────────────────────────────────┘
```

## Składnia SQL

```sql
BITMAP_XOR_COUNT( <bitmap> )
```

## Przykłady SQL

```sql
SELECT BITMAP_XOR_COUNT(TO_BITMAP('1, 3, 5'));

┌────────────────────────────────────────┐
│ bitmap_xor_count(to_bitmap('1, 3, 5')) │
├────────────────────────────────────────┤
│                                      3 │
└────────────────────────────────────────┘
```
