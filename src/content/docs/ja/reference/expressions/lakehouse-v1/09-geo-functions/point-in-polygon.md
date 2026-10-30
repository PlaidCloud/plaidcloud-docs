---
title: POINT_IN_POLYGON（Lakehouse v1）
description: POINT_IN_POLYGON — 指定した点が、複数の点を結んで形成されるポリゴンの内側にあるかどうかを計算します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/point-in-polygon.md
---

指定した点が、複数の点を結んで形成されるポリゴンの内側にあるかどうかを計算します。ポリゴンは、座標のペアを記載された順に結んでできる閉じた図形です。座標のペアの順序を変えると、異なる図形になることがあります。

## Analyze Syntax

```python
func.point_in_polygon((x,y), [(a,b), (c,d), (e,f) ... ])
```

## Analyze Examples

```python
func.point_in_polygon((3., 3.), [(6, 0), (8, 4), (5, 8), (0, 2)])

┌─────────────────────────────────────────────────────────────────┐
│ func.point_in_polygon((3, 3), [(6, 0), (8, 4), (5, 8), (0, 2)]) │
├─────────────────────────────────────────────────────────────────┤
│                                                               1 │
└─────────────────────────────────────────────────────────────────┘
```

## SQL Syntax

```sql
POINT_IN_POLYGON((x,y), [(a,b), (c,d), (e,f) ... ])
```

## SQL Examples

```sql
SELECT POINT_IN_POLYGON((3., 3.), [(6, 0), (8, 4), (5, 8), (0, 2)]);

┌────────────────────────────────────────────────────────────┐
│ point_in_polygon((3, 3), [(6, 0), (8, 4), (5, 8), (0, 2)]) │
├────────────────────────────────────────────────────────────┤
│                                                          1 │
└────────────────────────────────────────────────────────────┘
```
