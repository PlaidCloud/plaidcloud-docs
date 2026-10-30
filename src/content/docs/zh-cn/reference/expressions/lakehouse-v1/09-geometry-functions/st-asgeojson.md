---
title: ST_ASGEOJSON（Lakehouse v1）
description: ST_ASGEOJSON — 将 GEOMETRY 对象转换为 GeoJSON 表示。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-asgeojson.md
---

将 GEOMETRY 对象转换为 [GeoJSON](https://geojson.org/) 表示。

## SQL 语法

```sql
ST_ASGEOJSON(<geometry>)
```

## 参数

| 参数         | 说明                                   |
|--------------|----------------------------------------|
| `<geometry>` | 参数必须是 GEOMETRY 类型的表达式。     |

## 返回类型

Variant。

## SQL 示例

```sql
SELECT
  ST_ASGEOJSON(
    ST_GEOMETRYFROMWKT(
      'SRID=4326;LINESTRING(400000 6000000, 401000 6010000)'
    )
  ) AS pipeline_geojson;

┌─────────────────────────────────────────────────────────────────────────┐
│                             pipeline_geojson                            │
├─────────────────────────────────────────────────────────────────────────┤
│ {"coordinates":[[400000,6000000],[401000,6010000]],"type":"LineString"} │
└─────────────────────────────────────────────────────────────────────────┘
```
