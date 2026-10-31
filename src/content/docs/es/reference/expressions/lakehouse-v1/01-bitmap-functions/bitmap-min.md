---
title: BITMAP_MIN (Lakehouse v1)
description: BITMAP_MIN — obtiene el valor mínimo del mapa de bits.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-min.md
---

Obtiene el valor mínimo del mapa de bits.

## Sintaxis de Analyze

```python
func.bitmap_min( <bitmap> )
```

## Ejemplos de Analyze

```python
func.bitmap_min(func.build_bitmap([1, 4, 5]))

┌───────────────────────────────────────────────┐
│ func.bitmap_min(func.build_bitmap([1, 4, 5])) │
├───────────────────────────────────────────────┤
│                                             1 │
└───────────────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
BITMAP_MIN( <bitmap> )
```

## Ejemplos de SQL

```sql
SELECT BITMAP_MIN(BUILD_BITMAP([1,4,5]));

┌─────────────────────────────────────┐
│ bitmap_min(build_bitmap([1, 4, 5])) │
├─────────────────────────────────────┤
│                                   1 │
└─────────────────────────────────────┘
```
