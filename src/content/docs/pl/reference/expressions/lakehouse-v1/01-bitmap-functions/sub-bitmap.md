---
title: SUB_BITMAP (Lakehouse v1)
description: SUB_BITMAP — generuje podmapę bitową mapy źródłowej, zaczynając od indeksu początkowego, o określonym rozmiarze.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/sub-bitmap.md
---

Generuje podmapę bitową mapy źródłowej, zaczynając od indeksu początkowego, o określonym rozmiarze.

## Składnia Analyze

```python
func.sub_bitmap( <bitmap>, <start>, <size> )
```

## Przykłady Analyze

```python
func.sub_bitmap(func.build_bitmap([1, 2, 3, 4, 5]), 1, 3)

┌───────────────────────────────────────────────────────────┐
│ func.sub_bitmap(func.build_bitmap([1, 2, 3, 4, 5]), 1, 3) │
├───────────────────────────────────────────────────────────┤
│ 2,3,4                                                     │
└───────────────────────────────────────────────────────────┘
```

## Składnia SQL

```sql
SUB_BITMAP( <bitmap>, <start>, <size> )
```

## Przykłady SQL

```sql
SELECT SUB_BITMAP(BUILD_BITMAP([1, 2, 3, 4, 5]), 1, 3)::String;

┌─────────────────────────────────────────────────────────┐
│ sub_bitmap(build_bitmap([1, 2, 3, 4, 5]), 1, 3)::string │
├─────────────────────────────────────────────────────────┤
│ 2,3,4                                                   │
└─────────────────────────────────────────────────────────┘
```
