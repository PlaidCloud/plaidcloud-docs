---
title: H3_EDGE_LENGTH_M（Lakehouse v1）
description: H3_EDGE_LENGTH_M — 返回给定分辨率下六边形边的平均长度，单位为米。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-edge-length-m.md
---

返回给定分辨率下六边形边的平均长度，单位为米。不包括五边形。

## Analyze 语法

```python
func.h3_edge_length(1)
```

## Analyze 示例

```python
func.h3_edge_length(1)

┌──────────────────────────┐
│ func.h3_edge_length_m(1) │
├──────────────────────────┤
│        483056.8390711111 │
└──────────────────────────┘
```

## SQL 语法

```sql
H3_EDGE_LENGTH_M(1)
```

## SQL 示例

```sql
┌─────────────────────┐
│ h3_edge_length_m(1) │
├─────────────────────┤
│   483056.8390711111 │
└─────────────────────┘
```
