---
title: H3_GET_UNIDIRECTIONAL_EDGE_BOUNDARY（Lakehouse v1）
description: H3_GET_UNIDIRECTIONAL_EDGE_BOUNDARY — 返回定义单向边的坐标。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-get-unidirectional-edge-boundary.md
---

返回定义单向边的坐标。

## Analyze 语法

```python
func.h3_get_unidirectional_edge_boundary(h3)
```

## Analyze 示例

```python
func.h3_get_unidirectional_edge_boundary(1248204388774707199)

┌─────────────────────────────────────────────────────────────────────────────────┐
│           func.h3_get_unidirectional_edge_boundary(1248204388774707199)         │
├─────────────────────────────────────────────────────────────────────────────────┤
│ [(37.42012867767778,-122.03773496427027),(37.33755608435298,-122.090428929044)] │
└─────────────────────────────────────────────────────────────────────────────────┘
```

## SQL 语法

```sql
H3_GET_UNIDIRECTIONAL_EDGE_BOUNDARY(h3)
```

## SQL 示例

```sql
SELECT H3_GET_UNIDIRECTIONAL_EDGE_BOUNDARY(1248204388774707199);

┌─────────────────────────────────────────────────────────────────────────────────┐
│             h3_get_unidirectional_edge_boundary(1248204388774707199)            │
├─────────────────────────────────────────────────────────────────────────────────┤
│ [(37.42012867767778,-122.03773496427027),(37.33755608435298,-122.090428929044)] │
└─────────────────────────────────────────────────────────────────────────────────┘
```
