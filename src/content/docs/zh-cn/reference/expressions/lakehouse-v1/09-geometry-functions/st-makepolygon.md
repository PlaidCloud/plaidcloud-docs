---
title: ST_MAKEPOLYGON（Lakehouse v1）
description: ST_MAKEPOLYGON — 构造表示不含孔洞的 Polygon 的 GEOMETRY 对象。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-makepolygon.md
---

构造表示不含孔洞的 Polygon 的 GEOMETRY 对象。该函数使用指定的 LineString 作为外环。

## SQL 语法

```sql
ST_MAKEPOLYGON(<geometry>)
```

## 别名

- [ST_POLYGON](../st-polygon)

## 参数

| 参数         | 说明                                   |
|--------------|----------------------------------------|
| `<geometry>` | 参数必须是 GEOMETRY 类型的表达式。     |

## 返回类型

Geometry。

## SQL 示例

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
