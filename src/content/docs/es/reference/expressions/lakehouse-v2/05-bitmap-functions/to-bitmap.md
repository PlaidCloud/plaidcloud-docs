---
title: TO_BITMAP (Lakehouse v2)
description: TO_BITMAP — convierte un valor entero en un mapa de bits que contiene ese único valor.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/to-bitmap.md
---

Convierte un valor entero en un mapa de bits que contiene ese único valor.

## Sintaxis de Analyze

```python
func.to_bitmap(<value>)
```

## Ejemplos de Analyze

```python
func.to_bitmap(42)

┌──────────┐
│ (bitmap) │
└──────────┘
```

## Sintaxis de SQL

```sql
TO_BITMAP(<value>)
```

## Ejemplos de SQL

```sql
SELECT BITMAP_TO_STRING(TO_BITMAP(42));

┌────┐
│ 42 │
└────┘
```
