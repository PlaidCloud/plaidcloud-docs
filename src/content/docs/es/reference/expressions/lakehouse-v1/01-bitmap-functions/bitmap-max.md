---
title: BITMAP_MAX (Lakehouse v1)
description: BITMAP_MAX — obtiene el valor máximo del mapa de bits.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-max.md
---

Obtiene el valor máximo del mapa de bits.

## Sintaxis de Analyze

```python
func.bitmap_max( <bitmap> )
```

## Ejemplos de Analyze

```python
func.bitmap_max(func.build_bitmap([1, 4, 5]))

┌───────────────────────────────────────────────┐
│ func.bitmap_max(func.build_bitmap([1, 4, 5])) │
├───────────────────────────────────────────────┤
│                                             5 │
└───────────────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
BITMAP_MAX( <bitmap> )
```

## Ejemplos de SQL

```sql
SELECT BITMAP_MAX(BUILD_BITMAP([1,4,5]));

┌─────────────────────────────────────┐
│ bitmap_max(build_bitmap([1, 4, 5])) │
├─────────────────────────────────────┤
│                                   5 │
└─────────────────────────────────────┘
```
