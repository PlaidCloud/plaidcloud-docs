---
title: SUB_BITMAP (Lakehouse v1)
description: SUB_BITMAP – erzeugt eine Teil-Bitmap der Quell-Bitmap, die am Startindex beginnt und eine angegebene Größe hat.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/sub-bitmap.md
---

Erzeugt eine Teil-Bitmap der Quell-Bitmap, die am Startindex beginnt und eine angegebene Größe hat.

## Analyze-Syntax

```python
func.sub_bitmap( <bitmap>, <start>, <size> )
```

## Analyze-Beispiele

```python
func.sub_bitmap(func.build_bitmap([1, 2, 3, 4, 5]), 1, 3)

┌───────────────────────────────────────────────────────────┐
│ func.sub_bitmap(func.build_bitmap([1, 2, 3, 4, 5]), 1, 3) │
├───────────────────────────────────────────────────────────┤
│ 2,3,4                                                     │
└───────────────────────────────────────────────────────────┘
```

## SQL-Syntax

```sql
SUB_BITMAP( <bitmap>, <start>, <size> )
```

## SQL-Beispiele

```sql
SELECT SUB_BITMAP(BUILD_BITMAP([1, 2, 3, 4, 5]), 1, 3)::String;

┌─────────────────────────────────────────────────────────┐
│ sub_bitmap(build_bitmap([1, 2, 3, 4, 5]), 1, 3)::string │
├─────────────────────────────────────────────────────────┤
│ 2,3,4                                                   │
└─────────────────────────────────────────────────────────┘
```
