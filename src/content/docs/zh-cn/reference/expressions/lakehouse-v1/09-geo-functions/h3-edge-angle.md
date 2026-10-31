---
title: H3_EDGE_ANGLE（Lakehouse v1）
description: H3_EDGE_ANGLE — 返回 H3 六边形边的平均长度，单位为百分度。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-edge-angle.md
---

返回 H3 六边形边的平均长度，单位为百分度。

## Analyze 语法

```python
func.h3_edge_angle(res)
```

## Analyze 示例

```python
func.h3_edge_angle(10)

┌────────────────────────────┐
│   func.h3_edge_angle(10)   │
├────────────────────────────┤
│      0.0006822586214153981 │
└────────────────────────────┘
```

## SQL 语法

```sql
H3_EDGE_ANGLE(res)
```

## SQL 示例

```sql
SELECT H3_EDGE_ANGLE(10);

┌───────────────────────┐
│   h3_edge_angle(10)   │
├───────────────────────┤
│ 0.0006822586214153981 │
└───────────────────────┘
```
