---
title: H3_EDGE_LENGTH_KM（Lakehouse v1）
description: H3_EDGE_LENGTH_KM — 指定した解像度での六角形の辺の平均の長さをキロメートルで返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-edge-length-km.md
---

指定した解像度での六角形の辺の平均の長さをキロメートルで返します。五角形は含まれません。

## Analyze Syntax

```python
func.h3_edge_length_km(res)
```

## Analyze Examples

```python
func.h3_edge_length_km(1)

┌───────────────────────────┐
│ func.h3_edge_length_km(1) │
├───────────────────────────┤
│         483.0568390711111 │
└───────────────────────────┘
```

## SQL Syntax

```sql
H3_EDGE_LENGTH_KM(res)
```

## SQL Examples

```sql
SELECT H3_EDGE_LENGTH_KM(1);

┌──────────────────────┐
│ h3_edge_length_km(1) │
├──────────────────────┤
│    483.0568390711111 │
└──────────────────────┘
```
