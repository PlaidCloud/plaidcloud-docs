---
title: INTERSECT_COUNT (Lakehouse v2)
description: "Use la función de mapa de bits INTERSECT_COUNT en PlaidCloud Lakehouse. Devuelve el número de elementos de la intersección de varios mapas de bits filtrados por dimensión."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/intersect-count.md
---

Devuelve el número de elementos de la intersección de varios mapas de bits filtrados por dimensión.

## Sintaxis de Analyze

```python
func.intersect_count(get_column(table, 'bm'), get_column(table, 'dim'), val1, val2)
```

## Ejemplos de Analyze

```python
func.intersect_count(get_column(table, 'bm'), get_column(table, 'tag'), 1, 2)

┌─────┐
│ 150 │
└─────┘
```

## Sintaxis de SQL

```sql
INTERSECT_COUNT(<bm>, <dim>, val1, val2)
```

## Ejemplos de SQL

```sql
SELECT INTERSECT_COUNT(user_bm, tag, 1, 2) FROM segments;

┌─────┐
│ 150 │
└─────┘
```
