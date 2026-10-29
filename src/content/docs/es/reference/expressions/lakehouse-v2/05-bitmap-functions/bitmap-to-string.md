---
title: BITMAP_TO_STRING (Lakehouse v2)
description: BITMAP_TO_STRING — convierte un mapa de bits en una cadena separada por comas.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-to-string.md
---

Convierte un mapa de bits en una cadena separada por comas.

## Sintaxis de Analyze

```python
func.bitmap_to_string(<bitmap>)
```

## Ejemplos de Analyze

```python
func.bitmap_to_string(get_column(table, 'bm'))

┌─────────┐
│ '1,2,3' │
└─────────┘
```

## Sintaxis de SQL

```sql
BITMAP_TO_STRING(<bitmap>)
```

## Ejemplos de SQL

```sql
SELECT BITMAP_TO_STRING(BITMAP_FROM_STRING('1,2,3'));

┌───────┐
│ 1,2,3 │
└───────┘
```
