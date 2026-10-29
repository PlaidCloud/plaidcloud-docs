---
title: BITMAP_TO_ARRAY (Lakehouse v2)
description: BITMAP_TO_ARRAY — convierte un mapa de bits en una matriz de enteros.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-to-array.md
---

Convierte un mapa de bits en una matriz de enteros.

## Sintaxis de Analyze

```python
func.bitmap_to_array(<bitmap>)
```

## Ejemplos de Analyze

```python
func.bitmap_to_array(get_column(table, 'bm'))

┌─────────┐
│ [1,2,3] │
└─────────┘
```

## Sintaxis de SQL

```sql
BITMAP_TO_ARRAY(<bitmap>)
```

## Ejemplos de SQL

```sql
SELECT BITMAP_TO_ARRAY(BITMAP_FROM_STRING('1,2,3'));

┌─────────┐
│ [1,2,3] │
└─────────┘
```
