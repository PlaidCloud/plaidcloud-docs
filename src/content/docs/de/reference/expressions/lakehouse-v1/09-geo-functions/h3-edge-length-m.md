---
title: H3_EDGE_LENGTH_M (Lakehouse v1)
description: H3_EDGE_LENGTH_M — gibt die durchschnittliche Länge einer Hexagonkante in Metern bei der angegebenen Auflösung zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-edge-length-m.md
---

Gibt die durchschnittliche Länge einer Hexagonkante in Metern bei der angegebenen Auflösung zurück. Fünfecke sind ausgenommen.

## Analyze-Syntax

```python
func.h3_edge_length(1)
```

## Analyze-Beispiele

```python
func.h3_edge_length(1)

┌──────────────────────────┐
│ func.h3_edge_length_m(1) │
├──────────────────────────┤
│        483056.8390711111 │
└──────────────────────────┘
```

## SQL-Syntax

```sql
H3_EDGE_LENGTH_M(1)
```

## SQL-Beispiele

```sql
┌─────────────────────┐
│ h3_edge_length_m(1) │
├─────────────────────┤
│   483056.8390711111 │
└─────────────────────┘
```
