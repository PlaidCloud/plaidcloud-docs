---
title: H3_EXACT_EDGE_LENGTH_M (Lakehouse v1)
description: H3_EXACT_EDGE_LENGTH_M — calcula la longitud de esta arista dirigida, en metros.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-exact-edge-length-m.md
---

Calcula la longitud de esta arista dirigida, en metros.

## Sintaxis de Analyze

```python
func.h3_exact_edge_length_m(h3)
```

## Ejemplos de Analyze

```python
func.h3_exact_edge_length_m(1319695429381652479)

┌──────────────────────────────────────────────────┐
│ func.h3_exact_edge_length_m(1319695429381652479) │
├──────────────────────────────────────────────────┤
│                                8267.326832647143 │
└──────────────────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
H3_EXACT_EDGE_LENGTH_M(h3)
```

## Ejemplos de SQL

```sql
SELECT H3_EXACT_EDGE_LENGTH_M(1319695429381652479);

┌─────────────────────────────────────────────┐
│ h3_exact_edge_length_m(1319695429381652479) │
├─────────────────────────────────────────────┤
│                           8267.326832647143 │
└─────────────────────────────────────────────┘
```
