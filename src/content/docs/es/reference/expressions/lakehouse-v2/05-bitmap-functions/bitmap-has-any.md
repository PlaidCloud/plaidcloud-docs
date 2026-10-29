---
title: BITMAP_HAS_ANY (Lakehouse v2)
description: BITMAP_HAS_ANY — comprueba si dos mapas de bits tienen elementos en común.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-has-any.md
---

Comprueba si dos mapas de bits tienen elementos en común.

## Sintaxis de Analyze

```python
func.bitmap_has_any(<bm1>, <bm2>)
```

## Ejemplos de Analyze

```python
func.bitmap_has_any(get_column(table, 'bm1'), get_column(table, 'bm2'))

┌───┐
│ 1 │
└───┘
```

## Sintaxis de SQL

```sql
BITMAP_HAS_ANY(<bm1>, <bm2>)
```

## Ejemplos de SQL

```sql
SELECT BITMAP_HAS_ANY(BITMAP_FROM_STRING('1,2'), BITMAP_FROM_STRING('2,3'));

┌───┐
│ 1 │
└───┘
```
