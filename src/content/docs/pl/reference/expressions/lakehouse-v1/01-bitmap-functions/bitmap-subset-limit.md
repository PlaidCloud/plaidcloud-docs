---
title: BITMAP_SUBSET_LIMIT (Lakehouse v1)
description: BITMAP_SUBSET_LIMIT — generuje podmapę bitową mapy źródłowej, zaczynając od zakresu od wartości początkowej, z limitem rozmiaru.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-subset-limit.md
---

Generuje podmapę bitową mapy źródłowej, zaczynając od zakresu od wartości początkowej, z limitem rozmiaru.

## Składnia Analyze

```python
func.bitmap_subset_limit( <bitmap>, <start>, <limit> )
```

## Przykłady Analyze

```python
func.bitmap_subset_limit(func.build_bitmap([1, 4, 5]), 2, 2)

┌──────────────────────────────────────────────────────────────┐
│ func.bitmap_subset_limit(func.build_bitmap([1, 4, 5]), 2, 2) │
├──────────────────────────────────────────────────────────────┤
│ 4,5                                                          │
└──────────────────────────────────────────────────────────────┘
```

## Składnia SQL

```sql
BITMAP_SUBSET_LIMIT( <bitmap>, <start>, <limit> )
```

## Przykłady SQL

```sql
SELECT BITMAP_SUBSET_LIMIT(BUILD_BITMAP([1,4,5]), 2, 2)::String;

┌────────────────────────────────────────────────────────────┐
│ bitmap_subset_limit(build_bitmap([1, 4, 5]), 2, 2)::string │
├────────────────────────────────────────────────────────────┤
│ 4,5                                                        │
└────────────────────────────────────────────────────────────┘
```
