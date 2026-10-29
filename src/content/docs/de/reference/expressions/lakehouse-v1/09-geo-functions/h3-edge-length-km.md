---
title: H3_EDGE_LENGTH_KM (Lakehouse v1)
description: H3_EDGE_LENGTH_KM — gibt die durchschnittliche Länge einer Hexagonkante in Kilometern bei der angegebenen Auflösung zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-edge-length-km.md
---

Gibt die durchschnittliche Länge einer Hexagonkante in Kilometern bei der angegebenen Auflösung zurück. Fünfecke sind ausgenommen.

## Analyze-Syntax

```python
func.h3_edge_length_km(res)
```

## Analyze-Beispiele

```python
func.h3_edge_length_km(1)

┌───────────────────────────┐
│ func.h3_edge_length_km(1) │
├───────────────────────────┤
│         483.0568390711111 │
└───────────────────────────┘
```

## SQL-Syntax

```sql
H3_EDGE_LENGTH_KM(res)
```

## SQL-Beispiele

```sql
SELECT H3_EDGE_LENGTH_KM(1);

┌──────────────────────┐
│ h3_edge_length_km(1) │
├──────────────────────┤
│    483.0568390711111 │
└──────────────────────┘
```
