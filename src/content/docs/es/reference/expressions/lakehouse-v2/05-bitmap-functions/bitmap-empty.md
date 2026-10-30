---
title: BITMAP_EMPTY (Lakehouse v2)
description: BITMAP_EMPTY — devuelve un mapa de bits vacío.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-empty.md
---

Devuelve un mapa de bits vacío.

## Sintaxis de Analyze

```python
func.bitmap_empty()
```

## Ejemplos de Analyze

```python
func.bitmap_empty()

┌────────────────┐
│ (empty bitmap) │
└────────────────┘
```

## Sintaxis de SQL

```sql
BITMAP_EMPTY()
```

## Ejemplos de SQL

```sql
SELECT BITMAP_COUNT(BITMAP_EMPTY());

┌───┐
│ 0 │
└───┘
```
