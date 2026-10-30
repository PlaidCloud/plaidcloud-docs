---
title: ST_GEOHASH (Lakehouse v1)
description: ST_GEOHASH — 返回 GEOMETRY 对象的 geohash。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-geohash.md
---

返回 GEOMETRY 对象的 [geohash](https://en.wikipedia.org/wiki/Geohash)。geohash 是一个简短的 base32 字符串，用于标识包含世界上某个位置的大地矩形。可选的 precision 参数用于指定返回的 geohash 的 `precision`。例如，为 `precision 传入 5 会返回更短（5 个字符）但精度更低的 geohash。

## SQL 语法

```sql
ST_GEOHASH(<geometry> [, <precision>])
```

## 参数

| 参数       | 说明                                                               |
|-----------------|---------------------------------------------------------------------------|
| `geometry`    | 参数必须是 GEOMETRY 类型的表达式。                      |
| `[precision]` | 可选。指定返回的 geohash 的精度，默认为 12。 |

## 返回类型

字符串。

## SQL 示例

```sql
SELECT
  ST_GEOHASH(
    ST_GEOMETRYFROMWKT(
      'POINT(-122.306100 37.554162)'
    )
  ) AS pipeline_geohash;

┌──────────────────┐
│ pipeline_geohash │
├──────────────────┤
│ 9q9j8ue2v71y     │
└──────────────────┘

SELECT
  ST_GEOHASH(
    ST_GEOMETRYFROMWKT(
      'SRID=4326;POINT(-122.35 37.55)'
    ),
    5
  ) AS pipeline_geohash;

┌──────────────────┐
│ pipeline_geohash │
├──────────────────┤
│ 9q8vx            │
└──────────────────┘
```
