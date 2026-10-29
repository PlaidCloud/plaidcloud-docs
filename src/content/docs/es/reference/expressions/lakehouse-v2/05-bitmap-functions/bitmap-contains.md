---
title: BITMAP_CONTAINS (Lakehouse v2)
description: BITMAP_CONTAINS — comprueba si un mapa de bits contiene un valor específico.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-contains.md
---

Comprueba si un mapa de bits contiene un valor específico.

## Sintaxis de Analyze

```python
func.bitmap_contains(<bitmap>, <value>)
```

## Ejemplos de Analyze

```python
func.bitmap_contains(get_column(table, 'bm'), 42)

┌───┐
│ 1 │
└───┘
```

## Sintaxis de SQL

```sql
BITMAP_CONTAINS(<bitmap>, <value>)
```

## Ejemplos de SQL

```sql
SELECT BITMAP_CONTAINS(BITMAP_FROM_STRING('1,2,42'), 42);

┌───┐
│ 1 │
└───┘
```
