---
title: H3_GET_UNIDIRECTIONAL_EDGE_BOUNDARY (Lakehouse v1)
description: H3_GET_UNIDIRECTIONAL_EDGE_BOUNDARY — renvoie les coordonnées qui définissent l'arête unidirectionnelle.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-get-unidirectional-edge-boundary.md
---

Renvoie les coordonnées qui définissent l'arête unidirectionnelle.

## Syntaxe Analyze

```python
func.h3_get_unidirectional_edge_boundary(h3)
```

## Exemples Analyze

```python
func.h3_get_unidirectional_edge_boundary(1248204388774707199)

┌─────────────────────────────────────────────────────────────────────────────────┐
│           func.h3_get_unidirectional_edge_boundary(1248204388774707199)         │
├─────────────────────────────────────────────────────────────────────────────────┤
│ [(37.42012867767778,-122.03773496427027),(37.33755608435298,-122.090428929044)] │
└─────────────────────────────────────────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
H3_GET_UNIDIRECTIONAL_EDGE_BOUNDARY(h3)
```

## Exemples SQL

```sql
SELECT H3_GET_UNIDIRECTIONAL_EDGE_BOUNDARY(1248204388774707199);

┌─────────────────────────────────────────────────────────────────────────────────┐
│             h3_get_unidirectional_edge_boundary(1248204388774707199)            │
├─────────────────────────────────────────────────────────────────────────────────┤
│ [(37.42012867767778,-122.03773496427027),(37.33755608435298,-122.090428929044)] │
└─────────────────────────────────────────────────────────────────────────────────┘
```
