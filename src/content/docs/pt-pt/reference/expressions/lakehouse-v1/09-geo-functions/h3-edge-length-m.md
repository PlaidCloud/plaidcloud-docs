---
title: H3_EDGE_LENGTH_M (Lakehouse v1)
description: H3_EDGE_LENGTH_M — devolve o comprimento médio da aresta do hexágono em metros na resolução indicada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-edge-length-m.md
---

Devolve o comprimento médio da aresta do hexágono em metros na resolução indicada. Exclui pentágonos.

## Sintaxe do Analyze

```python
func.h3_edge_length(1)
```

## Exemplos do Analyze

```python
func.h3_edge_length(1)

┌──────────────────────────┐
│ func.h3_edge_length_m(1) │
├──────────────────────────┤
│        483056.8390711111 │
└──────────────────────────┘
```

## Sintaxe SQL

```sql
H3_EDGE_LENGTH_M(1)
```

## Exemplos de SQL

```sql
┌─────────────────────┐
│ h3_edge_length_m(1) │
├─────────────────────┤
│   483056.8390711111 │
└─────────────────────┘
```
