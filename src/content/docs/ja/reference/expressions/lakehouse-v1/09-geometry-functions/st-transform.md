---
title: ST_TRANSFORM（Lakehouse v1）
description: ST_TRANSFORM — GEOMETRYオブジェクトをある空間参照系（SRS）から別の空間参照系に変換します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-transform.md
---

GEOMETRYオブジェクトをある[空間参照系（SRS）](https://en.wikipedia.org/wiki/Spatial_reference_system)から別の空間参照系に変換します。座標を変更せずにSRIDだけを変更したい場合（たとえば、SRIDが誤っていた場合）は、代わりに[ST_SETSRID](../st-setsrid)を使用してください。

## SQL Syntax

```sql
ST_TRANSFORM(<geometry> [, <from_srid>], <to_srid>)
```

## 引数

| 引数     | 説明                                                                                                                                               |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| `<geometry>`  | GEOMETRYオブジェクト型の式を指定する必要があります。                                                                                               |
| `<from_srid>` | 入力GEOMETRYオブジェクトの現在のSRSを示すSRID（オプション）。この引数を省略した場合は、入力GEOMETRYオブジェクトで指定されているSRIDを使用します。 |
| `<to_srid>`   | 使用するSRSを示すSRID。入力GEOMETRYオブジェクトを、このSRSを使用する新しいオブジェクトに変換します。                                         |

## 戻り値の型

Geometry。

## SQL Examples

```sql
SET GEOMETRY_OUTPUT_FORMAT = 'EWKT'

SELECT ST_TRANSFORM(ST_GEOMFROMWKT('POINT(389866.35 5819003.03)', 32633), 3857) AS transformed_geom

┌───────────────────────────────────────────────┐
│                transformed_geom               │
├───────────────────────────────────────────────┤
│ SRID=3857;POINT(1489140.093766 6892872.19868) │
└───────────────────────────────────────────────┘

SELECT ST_TRANSFORM(ST_GEOMFROMWKT('POINT(4.500212 52.161170)'), 4326, 28992) AS transformed_geom

┌──────────────────────────────────────────────┐
│               transformed_geom               │
├──────────────────────────────────────────────┤
│ SRID=28992;POINT(94308.670475 464038.168827) │
└──────────────────────────────────────────────┘

```
