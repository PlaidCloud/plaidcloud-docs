---
title: ST_ASWKT（Lakehouse v1）
description: ST_ASWKT — GEOMETRYオブジェクトをWKT（well-known-text）形式の表現に変換します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-aswkt.md
---

GEOMETRYオブジェクトを[WKT（well-known-text）](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry)形式の表現に変換します。

## SQL Syntax

```sql
ST_ASWKT(<geometry>)
```

## エイリアス

- [ST_ASTEXT](../st-astext)

## 引数

| 引数    | 説明                                          |
|--------------|------------------------------------------------------|
| `<geometry>` | GEOMETRY型の式を指定する必要があります。 |

## 戻り値の型

String。

## SQL Examples

```sql
SELECT
  ST_ASWKT(
    ST_GEOMETRYFROMWKT(
      'SRID=4326;LINESTRING(400000 6000000, 401000 6010000)'
    )
  ) AS pipeline_wkt;

┌───────────────────────────────────────────┐
│                pipeline_wkt               │
├───────────────────────────────────────────┤
│ LINESTRING(400000 6000000,401000 6010000) │
└───────────────────────────────────────────┘

SELECT
  ST_ASTEXT(
    ST_GEOMETRYFROMWKT(
      'SRID=4326;POINT(-122.35 37.55)'
    )
  ) AS pipeline_wkt;

┌──────────────────────┐
│     pipeline_wkt     │
├──────────────────────┤
│ POINT(-122.35 37.55) │
└──────────────────────┘
```
