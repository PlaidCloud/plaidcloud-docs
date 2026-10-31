---
title: H3_EDGE_LENGTH_KM (Lakehouse v1)
description: H3_EDGE_LENGTH_KM — devolve o comprimento médio da aresta do hexágono em quilómetros na resolução indicada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-edge-length-km.md
---

Devolve o comprimento médio da aresta do hexágono em quilómetros na resolução indicada. Exclui pentágonos.

## Sintaxe do Analyze

```python
func.h3_edge_length_km(res)
```

## Exemplos do Analyze

```python
func.h3_edge_length_km(1)

┌───────────────────────────┐
│ func.h3_edge_length_km(1) │
├───────────────────────────┤
│         483.0568390711111 │
└───────────────────────────┘
```

## Sintaxe SQL

```sql
H3_EDGE_LENGTH_KM(res)
```

## Exemplos de SQL

```sql
SELECT H3_EDGE_LENGTH_KM(1);

┌──────────────────────┐
│ h3_edge_length_km(1) │
├──────────────────────┤
│    483.0568390711111 │
└──────────────────────┘
```
