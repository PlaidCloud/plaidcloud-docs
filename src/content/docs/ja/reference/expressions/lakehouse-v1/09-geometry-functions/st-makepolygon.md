---
title: ST_MAKEPOLYGON（Lakehouse v1）
description: ST_MAKEPOLYGON — 穴のないPolygonを表すGEOMETRYオブジェクトを作成します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-makepolygon.md
---

穴のないPolygonを表すGEOMETRYオブジェクトを作成します。この関数は、指定したLineStringを外側のループとして使用します。

## SQL Syntax

```sql
ST_MAKEPOLYGON(<geometry>)
```

## エイリアス

- [ST_POLYGON](../st-polygon)

## 引数

| 引数    | 説明                                          |
|--------------|------------------------------------------------------|
| `<geometry>` | GEOMETRY型の式を指定する必要があります。 |

## 戻り値の型

Geometry。

## SQL Examples

```sql
SELECT
  ST_MAKEPOLYGON(
    ST_GEOMETRYFROMWKT(
      'LINESTRING(0.0 0.0, 1.0 0.0, 1.0 2.0, 0.0 2.0, 0.0 0.0)'
    )
  ) AS pipeline_polygon;

┌────────────────────────────────┐
│        pipeline_polygon        │
├────────────────────────────────┤
│ POLYGON((0 0,1 0,1 2,0 2,0 0)) │
└────────────────────────────────┘
```
