---
title: H3_EDGE_ANGLE (Lakehouse v1)
description: H3_EDGE_ANGLE — devuelve la longitud media de la arista de un hexágono H3 en grados centesimales.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-edge-angle.md
---

Devuelve la longitud media de la arista de un hexágono H3 en grados centesimales.

## Sintaxis de Analyze

```python
func.h3_edge_angle(res)
```

## Ejemplos de Analyze

```python
func.h3_edge_angle(10)

┌────────────────────────────┐
│   func.h3_edge_angle(10)   │
├────────────────────────────┤
│      0.0006822586214153981 │
└────────────────────────────┘
```

## Sintaxis de SQL

```sql
H3_EDGE_ANGLE(res)
```

## Ejemplos de SQL

```sql
SELECT H3_EDGE_ANGLE(10);

┌───────────────────────┐
│   h3_edge_angle(10)   │
├───────────────────────┤
│ 0.0006822586214153981 │
└───────────────────────┘
```
