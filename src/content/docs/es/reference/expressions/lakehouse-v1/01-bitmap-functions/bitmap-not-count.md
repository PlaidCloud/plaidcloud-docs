---
title: BITMAP_NOT_COUNT (Lakehouse v1)
description: BITMAP_NOT_COUNT — cuenta el número de bits establecidos en 0 en el mapa de bits mediante una operación lógica NOT.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-not-count.md
---

Cuenta el número de bits establecidos en 0 en el mapa de bits mediante una operación lógica NOT.

## Sintaxis de Analyze

```python
func.bitmap_not_count( <bitmap> )
```

## Ejemplos de Analyze

```python
func.bitmap_not_count(func.to_bitmap('1, 3, 5'))

┌──────────────────────────────────────────────────┐
│ func.bitmap_not_count(func.to_bitmap('1, 3, 5')) │
├──────────────────────────────────────────────────┤
│                                                3 │
└──────────────────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
BITMAP_NOT_COUNT( <bitmap> )
```

## Ejemplos de SQL

```sql
SELECT BITMAP_NOT_COUNT(TO_BITMAP('1, 3, 5'));

┌────────────────────────────────────────┐
│ bitmap_not_count(to_bitmap('1, 3, 5')) │
├────────────────────────────────────────┤
│                                      3 │
└────────────────────────────────────────┘
```
