---
title: BITMAP_TO_BINARY (Lakehouse v2)
description: BITMAP_TO_BINARY — convierte un mapa de bits en un valor binario.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-to-binary.md
---

Convierte un mapa de bits en un valor binario.

## Sintaxis de Analyze

```python
func.bitmap_to_binary(<bitmap>)
```

## Ejemplos de Analyze

```python
func.bitmap_to_binary(get_column(table, 'bm'))

┌──────────┐
│ (binary) │
└──────────┘
```

## Sintaxis de SQL

```sql
BITMAP_TO_BINARY(<bitmap>)
```

## Ejemplos de SQL

```sql
SELECT HEX(BITMAP_TO_BINARY(BITMAP_FROM_STRING('1,2,3')));

┌──────────────┐
│ (hex string) │
└──────────────┘
```
