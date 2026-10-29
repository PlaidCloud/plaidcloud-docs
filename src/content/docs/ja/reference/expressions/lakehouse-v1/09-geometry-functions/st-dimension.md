---
title: ST_DIMENSION（Lakehouse v1）
description: ST_DIMENSION — ジオメトリオブジェクトの次元を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-dimension.md
---

ジオメトリオブジェクトの次元を返します。GEOMETRYオブジェクトの次元は次のとおりです。

| 地理空間オブジェクトタイプ       | 次元  |
|------------------------------|------------|
| Point / MultiPoint           | 0          |
| LineString / MultiLineString | 1          |
| Polygon / MultiPolygon       | 2          |

## SQL Syntax

```sql
ST_DIMENSION(<geometry>)
```

## 引数

| 引数    | 説明                                          |
|--------------|------------------------------------------------------|
| `<geometry>` | GEOMETRY型の式を指定する必要があります。 |

## 戻り値の型

UInt8。

## SQL Examples

```sql
SELECT
  ST_DIMENSION(
    ST_GEOMETRYFROMWKT(
      'POINT(-122.306100 37.554162)'
    )
  ) AS pipeline_dimension;

┌────────────────────┐
│ pipeline_dimension │
├────────────────────┤
│                  0 │
└────────────────────┘

SELECT
  ST_DIMENSION(
    ST_GEOMETRYFROMWKT(
      'LINESTRING(-124.20 42.00, -120.01 41.99)'
    )
  ) AS pipeline_dimension;

┌────────────────────┐
│ pipeline_dimension │
├────────────────────┤
│                  1 │
└────────────────────┘

SELECT
  ST_DIMENSION(
    ST_GEOMETRYFROMWKT(
      'POLYGON((-124.20 42.00, -120.01 41.99, -121.1 42.01, -124.20 42.00))'
    )
  ) AS pipeline_dimension;

┌────────────────────┐
│ pipeline_dimension │
├────────────────────┤
│                  2 │
└────────────────────┘
```
