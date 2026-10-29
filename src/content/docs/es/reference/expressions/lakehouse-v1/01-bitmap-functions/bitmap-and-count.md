---
title: BITMAP_AND_COUNT (Lakehouse v1)
description: BITMAP_AND_COUNT — cuenta el número de bits establecidos en 1 en el mapa de bits mediante una operación lógica AND.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-and-count.md
---

Cuenta el número de bits establecidos en 1 en el mapa de bits mediante una operación lógica AND.

## Sintaxis de Analyze

```python
func.bitmap_and_count( <bitmap> )
```

## Ejemplos de Analyze

```python
func.bitmap_and_count(to_bitmap('1, 3, 5'))

┌─────────────────────────────────────────────┐
│ func.bitmap_and_count(to_bitmap('1, 3, 5')) │
├─────────────────────────────────────────────┤
│                                           3 │
└─────────────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
BITMAP_AND_COUNT( <bitmap> )
```

## Ejemplos de SQL

```sql
SELECT BITMAP_AND_COUNT(TO_BITMAP('1, 3, 5'));

┌────────────────────────────────────────┐
│ bitmap_and_count(to_bitmap('1, 3, 5')) │
├────────────────────────────────────────┤
│                                      3 │
└────────────────────────────────────────┘
```
