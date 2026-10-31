---
title: H3_EDGE_LENGTH_M (Lakehouse v1)
description: H3_EDGE_LENGTH_M — renvoie la longueur moyenne de l'arête d'un hexagone, en mètres, à la résolution donnée.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-edge-length-m.md
---

Renvoie la longueur moyenne de l'arête d'un hexagone, en mètres, à la résolution donnée. Les pentagones sont exclus.

## Syntaxe Analyze

```python
func.h3_edge_length(1)
```

## Exemples Analyze

```python
func.h3_edge_length(1)

┌──────────────────────────┐
│ func.h3_edge_length_m(1) │
├──────────────────────────┤
│        483056.8390711111 │
└──────────────────────────┘
```

## Syntaxe SQL

```sql
H3_EDGE_LENGTH_M(1)
```

## Exemples SQL

```sql
┌─────────────────────┐
│ h3_edge_length_m(1) │
├─────────────────────┤
│   483056.8390711111 │
└─────────────────────┘
```
