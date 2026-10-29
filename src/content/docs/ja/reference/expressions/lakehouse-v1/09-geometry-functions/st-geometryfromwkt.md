---
title: ST_GEOMETRYFROMWKT（Lakehouse v1）
description: ST_GEOMETRYFROMWKT — WKT（well-known-text）またはEWKT（extended well-known-text）の入力を解析し、GEOMETRY型の値を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-geometryfromwkt.md
---

[WKT（well-known-text）](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry)または[EWKT（extended well-known-text）](https://postgis.net/docs/ST_GeomFromEWKT.html)の入力を解析し、GEOMETRY型の値を返します。

## SQL Syntax

```sql
ST_GEOMETRYFROMWKT(<string>, [<srid>])
```

## エイリアス

- [ST_GEOMFROMWKT](../st-geomfromwkt)
- [ST_GEOMETRYFROMEWKT](../st-geometryfromewkt)
- [ST_GEOMFROMEWKT](../st-geomfromewkt)
- [ST_GEOMFROMTEXT](../st-geomfromtext)
- [ST_GEOMETRYFROMTEXT](../st-geometryfromtext)

## 引数

| 引数   | 説明                                                     |
|-------------|-----------------------------------------------------------------|
| `<string>`  | WKTまたはEWKT形式の文字列式を指定する必要があります。 |
| `<srid>`    | 使用するSRIDの整数値。                           |

## 戻り値の型

Geometry。

## SQL Examples

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
