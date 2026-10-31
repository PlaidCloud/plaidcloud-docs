---
title: BITMAP_HASH (Lakehouse v2)
description: BITMAP_HASH — calcula un hash de 32 bits de un valor y devuelve un mapa de bits que contiene ese hash.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-hash.md
---

Calcula un hash de 32 bits de un valor y devuelve un mapa de bits que contiene ese hash.

## Sintaxis de Analyze

```python
func.bitmap_hash(<value>)
```

## Ejemplos de Analyze

```python
func.bitmap_hash('hello')

┌──────────┐
│ (bitmap) │
└──────────┘
```

## Sintaxis de SQL

```sql
BITMAP_HASH(<value>)
```

## Ejemplos de SQL

```sql
SELECT BITMAP_COUNT(BITMAP_HASH('hello'));

┌───┐
│ 1 │
└───┘
```
