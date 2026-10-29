---
title: H3_EDGE_ANGLE（Lakehouse v1）
description: H3_EDGE_ANGLE — H3六角形の辺の平均の長さをグラードで返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-edge-angle.md
---

H3六角形の辺の平均の長さをグラードで返します。

## Analyze Syntax

```python
func.h3_edge_angle(res)
```

## Analyze Examples

```python
func.h3_edge_angle(10)

┌────────────────────────────┐
│   func.h3_edge_angle(10)   │
├────────────────────────────┤
│      0.0006822586214153981 │
└────────────────────────────┘
```

## SQL Syntax

```sql
H3_EDGE_ANGLE(res)
```

## SQL Examples

```sql
SELECT H3_EDGE_ANGLE(10);

┌───────────────────────┐
│   h3_edge_angle(10)   │
├───────────────────────┤
│ 0.0006822586214153981 │
└───────────────────────┘
```
