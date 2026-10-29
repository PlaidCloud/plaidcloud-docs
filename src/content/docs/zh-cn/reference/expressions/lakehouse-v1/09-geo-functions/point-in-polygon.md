---
title: POINT_IN_POLYGON（Lakehouse v1）
description: POINT_IN_POLYGON — 计算给定点是否位于由多个点连接而成的多边形内。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/point-in-polygon.md
---

计算给定点是否位于由多个点连接而成的多边形内。多边形是由坐标对按出现顺序连接而成的封闭形状。更改坐标对的顺序可能会得到不同的形状。

## Analyze 语法

```python
func.point_in_polygon((x,y), [(a,b), (c,d), (e,f) ... ])
```

## Analyze 示例

```python
func.point_in_polygon((3., 3.), [(6, 0), (8, 4), (5, 8), (0, 2)])

┌─────────────────────────────────────────────────────────────────┐
│ func.point_in_polygon((3, 3), [(6, 0), (8, 4), (5, 8), (0, 2)]) │
├─────────────────────────────────────────────────────────────────┤
│                                                               1 │
└─────────────────────────────────────────────────────────────────┘
```

## SQL 语法

```sql
POINT_IN_POLYGON((x,y), [(a,b), (c,d), (e,f) ... ])
```

## SQL 示例

```sql
SELECT POINT_IN_POLYGON((3., 3.), [(6, 0), (8, 4), (5, 8), (0, 2)]);

┌────────────────────────────────────────────────────────────┐
│ point_in_polygon((3, 3), [(6, 0), (8, 4), (5, 8), (0, 2)]) │
├────────────────────────────────────────────────────────────┤
│                                                          1 │
└────────────────────────────────────────────────────────────┘
```
