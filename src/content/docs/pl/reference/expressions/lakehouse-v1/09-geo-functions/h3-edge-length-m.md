---
title: H3_EDGE_LENGTH_M (Lakehouse v1)
description: H3_EDGE_LENGTH_M — zwraca średnią długość krawędzi heksagonu w metrach dla danej rozdzielczości.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-edge-length-m.md
---

Zwraca średnią długość krawędzi heksagonu w metrach dla danej rozdzielczości. Nie obejmuje pentagonów.

## Składnia Analyze

```python
func.h3_edge_length(1)
```

## Przykłady Analyze

```python
func.h3_edge_length(1)

┌──────────────────────────┐
│ func.h3_edge_length_m(1) │
├──────────────────────────┤
│        483056.8390711111 │
└──────────────────────────┘
```

## Składnia SQL

```sql
H3_EDGE_LENGTH_M(1)
```

## Przykłady SQL

```sql
┌─────────────────────┐
│ h3_edge_length_m(1) │
├─────────────────────┤
│   483056.8390711111 │
└─────────────────────┘
```
