---
title: BITMAP_FROM_BINARY (Lakehouse v2)
description: BITMAP_FROM_BINARY — convierte un valor binario en un mapa de bits.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-from-binary.md
---

Convierte un valor binario en un mapa de bits.

## Sintaxis de Analyze

```python
func.bitmap_from_binary(<binary>)
```

## Ejemplos de Analyze

```python
func.bitmap_from_binary(get_column(table, 'bin_col'))

┌──────────┐
│ (bitmap) │
└──────────┘
```

## Sintaxis de SQL

```sql
BITMAP_FROM_BINARY(<binary>)
```

## Ejemplos de SQL

```sql
SELECT BITMAP_COUNT(BITMAP_FROM_BINARY(bm_binary)) FROM data;

┌───┐
│ 5 │
└───┘
```
