---
title: POINT_IN_POLYGON (Lakehouse v1)
description: POINT_IN_POLYGON — calcula se um ponto informado está dentro do polígono formado pela união de vários pontos.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/point-in-polygon.md
---

Calcula se um ponto informado está dentro do polígono formado pela união de vários pontos. Um polígono é uma forma fechada conectada por pares de coordenadas na ordem em que aparecem. Alterar a ordem dos pares de coordenadas pode resultar em uma forma diferente.

## Sintaxe do Analyze

```python
func.point_in_polygon((x,y), [(a,b), (c,d), (e,f) ... ])
```

## Exemplos do Analyze

```python
func.point_in_polygon((3., 3.), [(6, 0), (8, 4), (5, 8), (0, 2)])

┌─────────────────────────────────────────────────────────────────┐
│ func.point_in_polygon((3, 3), [(6, 0), (8, 4), (5, 8), (0, 2)]) │
├─────────────────────────────────────────────────────────────────┤
│                                                               1 │
└─────────────────────────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
POINT_IN_POLYGON((x,y), [(a,b), (c,d), (e,f) ... ])
```

## Exemplos de SQL

```sql
SELECT POINT_IN_POLYGON((3., 3.), [(6, 0), (8, 4), (5, 8), (0, 2)]);

┌────────────────────────────────────────────────────────────┐
│ point_in_polygon((3, 3), [(6, 0), (8, 4), (5, 8), (0, 2)]) │
├────────────────────────────────────────────────────────────┤
│                                                          1 │
└────────────────────────────────────────────────────────────┘
```
