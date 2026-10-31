---
title: H3_EDGE_LENGTH_KM（Lakehouse v1）
description: H3_EDGE_LENGTH_KM — 返回给定分辨率下六边形边的平均长度，单位为千米。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-edge-length-km.md
---

返回给定分辨率下六边形边的平均长度，单位为千米。不包括五边形。

## Analyze 语法

```python
func.h3_edge_length_km(res)
```

## Analyze 示例

```python
func.h3_edge_length_km(1)

┌───────────────────────────┐
│ func.h3_edge_length_km(1) │
├───────────────────────────┤
│         483.0568390711111 │
└───────────────────────────┘
```

## SQL 语法

```sql
H3_EDGE_LENGTH_KM(res)
```

## SQL 示例

```sql
SELECT H3_EDGE_LENGTH_KM(1);

┌──────────────────────┐
│ h3_edge_length_km(1) │
├──────────────────────┤
│    483.0568390711111 │
└──────────────────────┘
```
