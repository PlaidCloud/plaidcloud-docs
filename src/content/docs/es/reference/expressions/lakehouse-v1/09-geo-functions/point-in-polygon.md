---
title: POINT_IN_POLYGON (Lakehouse v1)
description: POINT_IN_POLYGON — calcula si un punto dado se encuentra dentro del polígono formado al unir varios puntos.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/point-in-polygon.md
---

Calcula si un punto dado se encuentra dentro del polígono formado al unir varios puntos. Un polígono es una forma cerrada que conecta pares de coordenadas en el orden en que aparecen. Cambiar el orden de los pares de coordenadas puede producir una forma distinta.

## Sintaxis de Analyze

```python
func.point_in_polygon((x,y), [(a,b), (c,d), (e,f) ... ])
```

## Ejemplos de Analyze

```python
func.point_in_polygon((3., 3.), [(6, 0), (8, 4), (5, 8), (0, 2)])

┌─────────────────────────────────────────────────────────────────┐
│ func.point_in_polygon((3, 3), [(6, 0), (8, 4), (5, 8), (0, 2)]) │
├─────────────────────────────────────────────────────────────────┤
│                                                               1 │
└─────────────────────────────────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
POINT_IN_POLYGON((x,y), [(a,b), (c,d), (e,f) ... ])
```

## Ejemplos de SQL

```sql
SELECT POINT_IN_POLYGON((3., 3.), [(6, 0), (8, 4), (5, 8), (0, 2)]);

┌────────────────────────────────────────────────────────────┐
│ point_in_polygon((3, 3), [(6, 0), (8, 4), (5, 8), (0, 2)]) │
├────────────────────────────────────────────────────────────┤
│                                                          1 │
└────────────────────────────────────────────────────────────┘
```
