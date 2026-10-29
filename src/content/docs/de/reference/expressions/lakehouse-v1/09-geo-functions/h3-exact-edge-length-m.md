---
title: H3_EXACT_EDGE_LENGTH_M (Lakehouse v1)
description: H3_EXACT_EDGE_LENGTH_M — berechnet die Länge dieser gerichteten Kante in Metern.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-exact-edge-length-m.md
---

Berechnet die Länge dieser gerichteten Kante in Metern.

## Analyze-Syntax

```python
func.h3_exact_edge_length_m(h3)
```

## Analyze-Beispiele

```python
func.h3_exact_edge_length_m(1319695429381652479)

┌──────────────────────────────────────────────────┐
│ func.h3_exact_edge_length_m(1319695429381652479) │
├──────────────────────────────────────────────────┤
│                                8267.326832647143 │
└──────────────────────────────────────────────────┘
```

## SQL-Syntax

```sql
H3_EXACT_EDGE_LENGTH_M(h3)
```

## SQL-Beispiele

```sql
SELECT H3_EXACT_EDGE_LENGTH_M(1319695429381652479);

┌─────────────────────────────────────────────┐
│ h3_exact_edge_length_m(1319695429381652479) │
├─────────────────────────────────────────────┤
│                           8267.326832647143 │
└─────────────────────────────────────────────┘
```
