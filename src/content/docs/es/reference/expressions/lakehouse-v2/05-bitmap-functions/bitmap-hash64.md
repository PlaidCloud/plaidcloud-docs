---
title: BITMAP_HASH64 (Lakehouse v2)
description: BITMAP_HASH64 — calcula un hash de 64 bits de un valor y devuelve un mapa de bits que contiene ese hash.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-hash64.md
---

Calcula un hash de 64 bits de un valor y devuelve un mapa de bits que contiene ese hash.

## Sintaxis de Analyze

```python
func.bitmap_hash64(<value>)
```

## Ejemplos de Analyze

```python
func.bitmap_hash64('hello')

┌──────────┐
│ (bitmap) │
└──────────┘
```

## Sintaxis de SQL

```sql
BITMAP_HASH64(<value>)
```

## Ejemplos de SQL

```sql
SELECT BITMAP_COUNT(BITMAP_HASH64('hello'));

┌───┐
│ 1 │
└───┘
```
