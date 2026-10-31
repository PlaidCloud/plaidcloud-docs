---
title: "TO_STRING（几何，Lakehouse v1）"
description: TO_STRING — 将 GEOMETRY 对象转换为字符串表示。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/to-string.md
---

将 GEOMETRY 对象转换为字符串表示。输出数据的显示格式由 `geometry_output_format` 设置控制，该设置包含以下类型：

| 参数              | 说明                                                  |
|-------------------|-------------------------------------------------------|
| GeoJSON（默认）   | GEOMETRY 结果呈现为 GeoJSON 格式的 JSON 对象。        |
| WKT               | GEOMETRY 结果呈现为 WKT 格式的字符串。                |
| WKB               | GEOMETRY 结果呈现为 WKB 格式的二进制。                |
| EWKT              | GEOMETRY 结果呈现为 EWKT 格式的字符串。               |
| EWKB              | GEOMETRY 结果呈现为 EWKB 格式的二进制。               |

## SQL 语法

```sql
TO_STRING(<geometry>)
```

## 参数

| 参数         | 说明                                   |
|--------------|----------------------------------------|
| `<geometry>` | 参数必须是 GEOMETRY 类型的表达式。     |

## 返回类型

String。

## SQL 示例

```sql
SET geometry_output_format='GeoJSON';

SELECT
  TO_GEOMETRY(
    ST_GEOMETRYFROMWKT(
      'SRID=4326;LINESTRING(400000 6000000, 401000 6010000)'
    )
  ) AS pipeline_geometry;

┌────────────────────────────────────────────────────────────────────────────┐
│                              pipeline_geometry                             │
├────────────────────────────────────────────────────────────────────────────┤
│ {"type": "LineString", "coordinates": [[400000,6000000],[401000,6010000]]} │
└────────────────────────────────────────────────────────────────────────────┘

SET geometry_output_format='WKT';

SELECT
  TO_GEOMETRY(
    ST_GEOMETRYFROMWKT(
      'SRID=4326;LINESTRING(400000 6000000, 401000 6010000)'
    )
  ) AS pipeline_geometry;

┌───────────────────────────────────────────┐
│             pipeline_geometry             │
├───────────────────────────────────────────┤
│ LINESTRING(400000 6000000,401000 6010000) │
└───────────────────────────────────────────┘

SET geometry_output_format='EWKT';

SELECT
  TO_GEOMETRY(
    ST_GEOMETRYFROMWKT(
      'SRID=4326;LINESTRING(400000 6000000, 401000 6010000)'
    )
  ) AS pipeline_geometry;

┌─────────────────────────────────────────────────────┐
│                  pipeline_geometry                  │
├─────────────────────────────────────────────────────┤
│ SRID=4326;LINESTRING(400000 6000000,401000 6010000) │
└─────────────────────────────────────────────────────┘

SET geometry_output_format='WKB';

SELECT
  TO_GEOMETRY(
    ST_GEOMETRYFROMWKT(
      'SRID=4326;LINESTRING(400000 6000000, 401000 6010000)'
    )
  ) AS pipeline_geometry;

┌────────────────────────────────────────────────────────────────────────────────────┐
│                                  pipeline_geometry                                 │
├────────────────────────────────────────────────────────────────────────────────────┤
│ 01020000000200000000000000006A18410000000060E3564100000000A07918410000000024ED5641 │
└────────────────────────────────────────────────────────────────────────────────────┘

SET geometry_output_format='EWKB';

SELECT
  TO_GEOMETRY(
    ST_GEOMETRYFROMWKT(
      'SRID=4326;LINESTRING(400000 6000000, 401000 6010000)'
    )
  ) AS pipeline_geometry;

┌────────────────────────────────────────────────────────────────────────────────────────────┐
│                                      pipeline_geometry                                     │
├────────────────────────────────────────────────────────────────────────────────────────────┤
│ 0102000020E61000000200000000000000006A18410000000060E3564100000000A07918410000000024ED5641 │
└────────────────────────────────────────────────────────────────────────────────────────────┘
```
