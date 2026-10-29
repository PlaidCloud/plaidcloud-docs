---
title: "ELEMENT_AT (Mapa, Lakehouse v2)"
description: ELEMENT_AT — devuelve el valor asociado a una clave específica de un mapa.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/element-at.md
---

Devuelve el valor asociado a una clave específica de un mapa.

## Sintaxis de Analyze

```python
func.element_at(get_column(table, 'map_col'), 'key')
```

## Ejemplos de Analyze

```python
func.element_at(MAP{'a':1,'b':2}, 'b')

┌───┐
│ 2 │
└───┘
```

## Sintaxis de SQL

```sql
ELEMENT_AT(<map_col>, 'key')
```

## Ejemplos de SQL

```sql
SELECT ELEMENT_AT(MAP{'a':1, 'b':2}, 'b');

┌───┐
│ 2 │
└───┘
```
