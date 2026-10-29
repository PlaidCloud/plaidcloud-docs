---
title: H3_EDGE_LENGTH_KM (Lakehouse v1)
description: H3_EDGE_LENGTH_KM — renvoie la longueur moyenne de l'arête d'un hexagone, en kilomètres, à la résolution donnée.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-edge-length-km.md
---

Renvoie la longueur moyenne de l'arête d'un hexagone, en kilomètres, à la résolution donnée. Les pentagones sont exclus.

## Syntaxe Analyze

```python
func.h3_edge_length_km(res)
```

## Exemples Analyze

```python
func.h3_edge_length_km(1)

┌───────────────────────────┐
│ func.h3_edge_length_km(1) │
├───────────────────────────┤
│         483.0568390711111 │
└───────────────────────────┘
```

## Syntaxe SQL

```sql
H3_EDGE_LENGTH_KM(res)
```

## Exemples SQL

```sql
SELECT H3_EDGE_LENGTH_KM(1);

┌──────────────────────┐
│ h3_edge_length_km(1) │
├──────────────────────┤
│    483.0568390711111 │
└──────────────────────┘
```
