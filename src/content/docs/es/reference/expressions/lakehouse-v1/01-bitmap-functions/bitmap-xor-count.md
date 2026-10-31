---
title: BITMAP_XOR_COUNT (Lakehouse v1)
description: BITMAP_XOR_COUNT — cuenta el número de bits establecidos en 1 en el mapa de bits mediante una operación lógica XOR.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-xor-count.md
---

Cuenta el número de bits establecidos en 1 en el mapa de bits mediante una operación lógica XOR (OR exclusivo).

## Sintaxis de Analyze

```python
func.bitmap_xor_count( <bitmap> )
```

## Ejemplos de Analyze

```python
func.bitmap_xor_count(func.to_bitmap('1, 3, 5'))

┌──────────────────────────────────────────────────┐
│ func.bitmap_xor_count(func.to_bitmap('1, 3, 5')) │
├──────────────────────────────────────────────────┤
│                                                3 │
└──────────────────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
BITMAP_XOR_COUNT( <bitmap> )
```

## Ejemplos de SQL

```sql
SELECT BITMAP_XOR_COUNT(TO_BITMAP('1, 3, 5'));

┌────────────────────────────────────────┐
│ bitmap_xor_count(to_bitmap('1, 3, 5')) │
├────────────────────────────────────────┤
│                                      3 │
└────────────────────────────────────────┘
```
