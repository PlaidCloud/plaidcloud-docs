---
title: BASE64_TO_BITMAP (Lakehouse v2)
description: BASE64_TO_BITMAP — convierte una cadena codificada en base64 en un mapa de bits.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/base64-to-bitmap.md
---

Convierte una cadena codificada en base64 en un mapa de bits.

## Sintaxis de Analyze

```python
func.base64_to_bitmap(<str>)
```

## Ejemplos de Analyze

```python
func.base64_to_bitmap(get_column(table, 'b64_col'))

┌──────────┐
│ (bitmap) │
└──────────┘
```

## Sintaxis de SQL

```sql
BASE64_TO_BITMAP(<str>)
```

## Ejemplos de SQL

```sql
SELECT BITMAP_TO_STRING(BASE64_TO_BITMAP(b64_col)) FROM data;

┌───────┐
│ 1,2,3 │
└───────┘
```
