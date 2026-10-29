---
title: H3_EXACT_EDGE_LENGTH_RADS (Lakehouse v1)
description: H3_EXACT_EDGE_LENGTH_RADS — calcule la longueur de cette arête orientée, en radians.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-exact-edge-length-rads.md
---

Calcule la longueur de cette arête orientée, en radians.

## Syntaxe Analyze

```python
func.h3_exact_edge_length_km(h3)
```

## Exemples Analyze

```python
func.h3_exact_edge_length_km(1319695429381652479)

┌───────────────────────────────────────────────────┐
│ func.h3_exact_edge_length_km(1319695429381652479) │
├───────────────────────────────────────────────────┤
│                                 8.267326832647143 │
└───────────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
H3_EXACT_EDGE_LENGTH_RADS(h3)
```

## Exemples SQL

```sql
SELECT H3_EXACT_EDGE_LENGTH_KM(1319695429381652479);

┌──────────────────────────────────────────────┐
│ h3_exact_edge_length_km(1319695429381652479) │
├──────────────────────────────────────────────┤
│                            8.267326832647143 │
└──────────────────────────────────────────────┘
```
