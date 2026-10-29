---
title: H3_EDGE_ANGLE (Lakehouse v1)
description: H3_EDGE_ANGLE — devolve o comprimento médio da aresta do hexágono H3 em grados.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-edge-angle.md
---

Devolve o comprimento médio da aresta do hexágono H3 em grados.

## Sintaxe do Analyze

```python
func.h3_edge_angle(res)
```

## Exemplos do Analyze

```python
func.h3_edge_angle(10)

┌────────────────────────────┐
│   func.h3_edge_angle(10)   │
├────────────────────────────┤
│      0.0006822586214153981 │
└────────────────────────────┘
```

## Sintaxe SQL

```sql
H3_EDGE_ANGLE(res)
```

## Exemplos de SQL

```sql
SELECT H3_EDGE_ANGLE(10);

┌───────────────────────┐
│   h3_edge_angle(10)   │
├───────────────────────┤
│ 0.0006822586214153981 │
└───────────────────────┘
```
