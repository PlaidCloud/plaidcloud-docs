---
title: ST_GEOMETRYFROMWKT（Lakehouse v1）
description: ST_GEOMETRYFROMWKT — 解析 WKT（众所周知的文本）或 EWKT（扩展众所周知的文本）输入，并返回 GEOMETRY 类型的值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-geometryfromwkt.md
---

解析 [WKT（众所周知的文本）](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry)或 [EWKT（扩展众所周知的文本）](https://postgis.net/docs/ST_GeomFromEWKT.html)输入，并返回 GEOMETRY 类型的值。

## SQL 语法

```sql
ST_GEOMETRYFROMWKT(<string>, [<srid>])
```

## 别名

- [ST_GEOMFROMWKT](../st-geomfromwkt)
- [ST_GEOMETRYFROMEWKT](../st-geometryfromewkt)
- [ST_GEOMFROMEWKT](../st-geomfromewkt)
- [ST_GEOMFROMTEXT](../st-geomfromtext)
- [ST_GEOMETRYFROMTEXT](../st-geometryfromtext)

## 参数

| 参数        | 说明                                           |
|-------------|------------------------------------------------|
| `<string>`  | 参数必须是 WKT 或 EWKT 格式的字符串表达式。    |
| `<srid>`    | 要使用的 SRID 的整数值。                       |

## 返回类型

Geometry。

## SQL 示例

```sql
SELECT
  ST_GEOMETRYFROMWKT(
    'POINT(1820.12 890.56)'
  ) AS pipeline_geometry;

┌───────────────────────┐
│   pipeline_geometry   │
├───────────────────────┤
│ POINT(1820.12 890.56) │
└───────────────────────┘

SELECT
  ST_GEOMETRYFROMWKT(
    'POINT(1820.12 890.56)', 4326
  ) AS pipeline_geometry;

┌─────────────────────────────────┐
│        pipeline_geometry        │
│             Geometry            │
├─────────────────────────────────┤
│ SRID=4326;POINT(1820.12 890.56) │
└─────────────────────────────────┘
```
