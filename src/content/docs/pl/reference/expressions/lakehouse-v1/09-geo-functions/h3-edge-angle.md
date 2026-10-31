---
title: H3_EDGE_ANGLE (Lakehouse v1)
description: H3_EDGE_ANGLE — zwraca średnią długość krawędzi heksagonu H3 w gradach.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-edge-angle.md
---

Zwraca średnią długość krawędzi heksagonu H3 w gradach.

## Składnia Analyze

```python
func.h3_edge_angle(res)
```

## Przykłady Analyze

```python
func.h3_edge_angle(10)

┌────────────────────────────┐
│   func.h3_edge_angle(10)   │
├────────────────────────────┤
│      0.0006822586214153981 │
└────────────────────────────┘
```

## Składnia SQL

```sql
H3_EDGE_ANGLE(res)
```

## Przykłady SQL

```sql
SELECT H3_EDGE_ANGLE(10);

┌───────────────────────┐
│   h3_edge_angle(10)   │
├───────────────────────┤
│ 0.0006822586214153981 │
└───────────────────────┘
```
