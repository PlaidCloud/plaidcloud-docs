---
title: H3_EXACT_EDGE_LENGTH_RADS (Lakehouse v1)
description: H3_EXACT_EDGE_LENGTH_RADS — berechnet die Länge dieser gerichteten Kante in Radiant.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-exact-edge-length-rads.md
---

Berechnet die Länge dieser gerichteten Kante in Radiant.

## Analyze-Syntax

```python
func.h3_exact_edge_length_km(h3)
```

## Analyze-Beispiele

```python
func.h3_exact_edge_length_km(1319695429381652479)

┌───────────────────────────────────────────────────┐
│ func.h3_exact_edge_length_km(1319695429381652479) │
├───────────────────────────────────────────────────┤
│                                 8.267326832647143 │
└───────────────────────────────────────────────────┘
```

## SQL-Syntax

```sql
H3_EXACT_EDGE_LENGTH_RADS(h3)
```

## SQL-Beispiele

```sql
SELECT H3_EXACT_EDGE_LENGTH_KM(1319695429381652479);

┌──────────────────────────────────────────────┐
│ h3_exact_edge_length_km(1319695429381652479) │
├──────────────────────────────────────────────┤
│                            8.267326832647143 │
└──────────────────────────────────────────────┘
```
