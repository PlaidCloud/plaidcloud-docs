---
title: H3_EXACT_EDGE_LENGTH_KM (Lakehouse v1)
description: H3_EXACT_EDGE_LENGTH_KM — oblicza długość tej krawędzi skierowanej w kilometrach.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-exact-edge-length-km.md
---

Oblicza długość tej krawędzi skierowanej w kilometrach.

## Składnia Analyze

```python
func.h3_exact_edge_length_km(h3)
```

## Przykłady Analyze

```python
func.h3_exact_edge_length_km(1319695429381652479)

┌───────────────────────────────────────────────────┐
│ func.h3_exact_edge_length_km(1319695429381652479) │
├───────────────────────────────────────────────────┤
│                                 8.267326832647143 │
└───────────────────────────────────────────────────┘
```

## Składnia SQL

```sql
H3_EXACT_EDGE_LENGTH_KM(h3)
```

## Przykłady SQL

```sql
SELECT H3_EXACT_EDGE_LENGTH_KM(1319695429381652479);

┌──────────────────────────────────────────────┐
│ h3_exact_edge_length_km(1319695429381652479) │
├──────────────────────────────────────────────┤
│                            8.267326832647143 │
└──────────────────────────────────────────────┘
```
