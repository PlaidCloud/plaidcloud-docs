---
title: H3_EDGE_ANGLE (Lakehouse v1)
description: H3_EDGE_ANGLE — gibt die durchschnittliche Länge der H3-Hexagonkante in Gon zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-edge-angle.md
---

Gibt die durchschnittliche Länge der H3-Hexagonkante in Gon zurück.

## Analyze-Syntax

```python
func.h3_edge_angle(res)
```

## Analyze-Beispiele

```python
func.h3_edge_angle(10)

┌────────────────────────────┐
│   func.h3_edge_angle(10)   │
├────────────────────────────┤
│      0.0006822586214153981 │
└────────────────────────────┘
```

## SQL-Syntax

```sql
H3_EDGE_ANGLE(res)
```

## SQL-Beispiele

```sql
SELECT H3_EDGE_ANGLE(10);

┌───────────────────────┐
│   h3_edge_angle(10)   │
├───────────────────────┤
│ 0.0006822586214153981 │
└───────────────────────┘
```
