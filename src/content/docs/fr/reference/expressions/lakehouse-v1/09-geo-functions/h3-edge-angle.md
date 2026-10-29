---
title: H3_EDGE_ANGLE (Lakehouse v1)
description: H3_EDGE_ANGLE — renvoie la longueur moyenne de l'arête d'un hexagone H3, en grades.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-edge-angle.md
---

Renvoie la longueur moyenne de l'arête d'un hexagone H3, en grades.

## Syntaxe Analyze

```python
func.h3_edge_angle(res)
```

## Exemples Analyze

```python
func.h3_edge_angle(10)

┌────────────────────────────┐
│   func.h3_edge_angle(10)   │
├────────────────────────────┤
│      0.0006822586214153981 │
└────────────────────────────┘
```

## Syntaxe SQL

```sql
H3_EDGE_ANGLE(res)
```

## Exemples SQL

```sql
SELECT H3_EDGE_ANGLE(10);

┌───────────────────────┐
│   h3_edge_angle(10)   │
├───────────────────────┤
│ 0.0006822586214153981 │
└───────────────────────┘
```
