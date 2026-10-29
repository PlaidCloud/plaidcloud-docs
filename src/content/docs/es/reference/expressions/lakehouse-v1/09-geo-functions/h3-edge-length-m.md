---
title: H3_EDGE_LENGTH_M (Lakehouse v1)
description: H3_EDGE_LENGTH_M — devuelve la longitud media de la arista de un hexágono en metros para la resolución dada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-edge-length-m.md
---

Devuelve la longitud media de la arista de un hexágono en metros para la resolución dada. Excluye los pentágonos.

## Sintaxis de Analyze

```python
func.h3_edge_length(1)
```

## Ejemplos de Analyze

```python
func.h3_edge_length(1)

┌──────────────────────────┐
│ func.h3_edge_length_m(1) │
├──────────────────────────┤
│        483056.8390711111 │
└──────────────────────────┘
```

## Sintaxis de SQL

```sql
H3_EDGE_LENGTH_M(1)
```

## Ejemplos de SQL

```sql
┌─────────────────────┐
│ h3_edge_length_m(1) │
├─────────────────────┤
│   483056.8390711111 │
└─────────────────────┘
```
