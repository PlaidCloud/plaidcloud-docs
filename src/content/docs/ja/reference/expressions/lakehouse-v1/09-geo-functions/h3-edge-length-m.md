---
title: H3_EDGE_LENGTH_M（Lakehouse v1）
description: H3_EDGE_LENGTH_M — 指定した解像度での六角形の辺の平均の長さをメートルで返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-edge-length-m.md
---

指定した解像度での六角形の辺の平均の長さをメートルで返します。五角形は含まれません。

## Analyze Syntax

```python
func.h3_edge_length(1)
```

## Analyze Examples

```python
func.h3_edge_length(1)

┌──────────────────────────┐
│ func.h3_edge_length_m(1) │
├──────────────────────────┤
│        483056.8390711111 │
└──────────────────────────┘
```

## SQL Syntax

```sql
H3_EDGE_LENGTH_M(1)
```

## SQL Examples

```sql
┌─────────────────────┐
│ h3_edge_length_m(1) │
├─────────────────────┤
│   483056.8390711111 │
└─────────────────────┘
```
