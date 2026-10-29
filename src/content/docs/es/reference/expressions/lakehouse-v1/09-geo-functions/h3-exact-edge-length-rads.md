---
title: H3_EXACT_EDGE_LENGTH_RADS (Lakehouse v1)
description: H3_EXACT_EDGE_LENGTH_RADS — calcula la longitud de esta arista dirigida, en radianes.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-exact-edge-length-rads.md
---

Calcula la longitud de esta arista dirigida, en radianes.

## Sintaxis de Analyze

```python
func.h3_exact_edge_length_km(h3)
```

## Ejemplos de Analyze

```python
func.h3_exact_edge_length_km(1319695429381652479)

┌───────────────────────────────────────────────────┐
│ func.h3_exact_edge_length_km(1319695429381652479) │
├───────────────────────────────────────────────────┤
│                                 8.267326832647143 │
└───────────────────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
H3_EXACT_EDGE_LENGTH_RADS(h3)
```

## Ejemplos de SQL

```sql
SELECT H3_EXACT_EDGE_LENGTH_KM(1319695429381652479);

┌──────────────────────────────────────────────┐
│ h3_exact_edge_length_km(1319695429381652479) │
├──────────────────────────────────────────────┤
│                            8.267326832647143 │
└──────────────────────────────────────────────┘
```
