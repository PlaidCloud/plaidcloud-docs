---
title: BITMAP_CONTAINS (Lakehouse v1)
description: BITMAP_CONTAINS — sprawdza, czy mapa bitowa zawiera określoną wartość.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-contains.md
---

Sprawdza, czy mapa bitowa zawiera określoną wartość.


## Składnia Analyze

```python
func.bitmap_contains( <bitmap>, <value> )
```

## Przykłady Analyze

```python
func.bitmap_contains(build_bitmap([1, 4, 5]), 1)

┌───────────────────────────────────────────────────┐
│ func.bitmap_contains(build_bitmap([1, 4, 5]), 1)  │
├───────────────────────────────────────────────────┤
│ true                                              │
└───────────────────────────────────────────────────┘
```

## Składnia SQL

```sql
BITMAP_CONTAINS( <bitmap>, <value> )
```

## Przykłady SQL

```sql
SELECT BITMAP_CONTAINS(BUILD_BITMAP([1,4,5]), 1);

┌─────────────────────────────────────────────┐
│ bitmap_contains(build_bitmap([1, 4, 5]), 1) │
├─────────────────────────────────────────────┤
│ true                                        │
└─────────────────────────────────────────────┘
```
