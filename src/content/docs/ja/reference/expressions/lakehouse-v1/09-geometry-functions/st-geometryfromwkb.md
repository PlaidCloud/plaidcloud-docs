---
title: ST_GEOMETRYFROMWKB（Lakehouse v1）
description: ST_GEOMETRYFROMWKB — WKB（well-known-binary）またはEWKB（extended well-known-binary）の入力を解析します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-geometryfromwkb.md
---

[WKB（well-known-binary）](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry#Well-known_binary)または[EWKB（extended well-known-binary）](https://postgis.net/docs/ST_GeomFromEWKB.html)の入力を解析し、GEOMETRY型の値を返します。

## SQL Syntax

```sql
ST_GEOMETRYFROMWKB(<string>, [<srid>])
ST_GEOMETRYFROMWKB(<binary>, [<srid>])
```

## エイリアス

- [ST_GEOMFROMWKB](../st-geomfromwkb)
- [ST_GEOMETRYFROMEWKB](../st-geometryfromewkb)
- [ST_GEOMFROMEWKB](../st-geomfromewkb)

## 引数

| 引数   | 説明                                                                    |
|-------------|--------------------------------------------------------------------------------|
| `<string>`  | 16進数形式のWKBまたはEWKBの文字列式を指定する必要があります。 |
| `<binary>`  | WKBまたはEWKB形式のバイナリ式を指定する必要があります。                |
| `<srid>`    | 使用するSRIDの整数値。                                          |

## 戻り値の型

Geometry。

## SQL Examples

```sql
SELECT
  ST_GEOMETRYFROMWKB(
    '0101000020797f000066666666a9cb17411f85ebc19e325641'
  ) AS pipeline_geometry;

┌────────────────────────────────────────┐
│            pipeline_geometry           │
├────────────────────────────────────────┤
│ SRID=32633;POINT(389866.35 5819003.03) │
└────────────────────────────────────────┘

SELECT
  ST_GEOMETRYFROMWKB(
    FROM_HEX('0101000020797f000066666666a9cb17411f85ebc19e325641'), 4326
  ) AS pipeline_geometry;

┌───────────────────────────────────────┐
│           pipeline_geometry           │
├───────────────────────────────────────┤
│ SRID=4326;POINT(389866.35 5819003.03) │
└───────────────────────────────────────┘
```
