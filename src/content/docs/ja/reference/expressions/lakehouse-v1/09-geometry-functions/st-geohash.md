---
title: ST_GEOHASH (Lakehouse v1)
description: ST_GEOHASH — GEOMETRY オブジェクトの geohash を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-geohash.md
---

GEOMETRY オブジェクトの [geohash](https://en.wikipedia.org/wiki/Geohash) を返します。geohash は、世界中の位置を含む測地線上の矩形を識別する、短い base32 文字列です。オプションの精度引数で、返される geohash の `precision` を指定します。たとえば、`precision に 5 を渡すと、より短く（5 文字）精度の低い geohash が返されます。

## SQL 構文

```sql
ST_GEOHASH(<geometry> [, <precision>])
```

## 引数

| 引数       | 説明                                                               |
|-----------------|---------------------------------------------------------------------------|
| `geometry`    | GEOMETRY 型の式を指定する必要があります。                      |
| `[precision]` | オプション。返される geohash の精度を指定します。デフォルトは 12 です。 |

## 戻り値の型

String。

## SQL の例

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
