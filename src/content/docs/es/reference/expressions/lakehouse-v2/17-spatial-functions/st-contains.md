---
title: ST_CONTAINS (Lakehouse v2)
description: ST_CONTAINS — comprueba si una geometría contiene a otra. Devuelve 1 si es verdadero.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/17-spatial-functions/st-contains.md
---

Comprueba si una geometría contiene a otra. Devuelve 1 si es verdadero.

## Sintaxis de Analyze

```python
func.st_contains(<geometry1>, <geometry2>)
```

## Ejemplos de Analyze

```python
func.st_contains(get_column(table, 'area'), func.st_point(1, 1))

┌───┐
│ 1  │
└───┘
```

## Sintaxis de SQL

```sql
ST_CONTAINS(<geometry1>, <geometry2>)
```

## Ejemplos de SQL

```sql
SELECT ST_CONTAINS(ST_GeomFromText('POLYGON((0 0,10 0,10 10,0 10,0 0))'), ST_POINT(5, 5));

┌───┐
│ 1  │
└───┘
```
