---
title: BITMAP_MIN (Lakehouse v1)
description: BITMAP_MIN — obtém o valor mínimo do bitmap.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-min.md
---

Obtém o valor mínimo do bitmap.

## Sintaxe do Analyze

```python
func.bitmap_min( <bitmap> )
```

## Exemplos do Analyze

```python
func.bitmap_min(func.build_bitmap([1, 4, 5]))

┌───────────────────────────────────────────────┐
│ func.bitmap_min(func.build_bitmap([1, 4, 5])) │
├───────────────────────────────────────────────┤
│                                             1 │
└───────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
BITMAP_MIN( <bitmap> )
```

## Exemplos SQL

```sql
SELECT BITMAP_MIN(BUILD_BITMAP([1,4,5]));

┌─────────────────────────────────────┐
│ bitmap_min(build_bitmap([1, 4, 5])) │
├─────────────────────────────────────┤
│                                   1 │
└─────────────────────────────────────┘
```
