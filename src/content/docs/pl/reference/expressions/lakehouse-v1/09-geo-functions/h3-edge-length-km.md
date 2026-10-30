---
title: H3_EDGE_LENGTH_KM (Lakehouse v1)
description: H3_EDGE_LENGTH_KM — zwraca średnią długość krawędzi heksagonu w kilometrach dla danej rozdzielczości.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-edge-length-km.md
---

Zwraca średnią długość krawędzi heksagonu w kilometrach dla danej rozdzielczości. Nie obejmuje pentagonów.

## Składnia Analyze

```python
func.h3_edge_length_km(res)
```

## Przykłady Analyze

```python
func.h3_edge_length_km(1)

┌───────────────────────────┐
│ func.h3_edge_length_km(1) │
├───────────────────────────┤
│         483.0568390711111 │
└───────────────────────────┘
```

## Składnia SQL

```sql
H3_EDGE_LENGTH_KM(res)
```

## Przykłady SQL

```sql
SELECT H3_EDGE_LENGTH_KM(1);

┌──────────────────────┐
│ h3_edge_length_km(1) │
├──────────────────────┤
│    483.0568390711111 │
└──────────────────────┘
```
