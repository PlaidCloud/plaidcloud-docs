---
title: ST_GEOMPOINTFROMGEOHASH（Lakehouse v1）
description: ST_GEOMPOINTFROMGEOHASH — geohashの中心を表す点のGEOMETRYオブジェクトを返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-geompointfromgeohash.md
---

[geohash](https://en.wikipedia.org/wiki/Geohash)の中心を表す点のGEOMETRYオブジェクトを返します。

## SQL Syntax

```sql
ST_GEOMPOINTFROMGEOHASH(<geohash>)
```

## 引数

| 引数   | 説明                     |
|-------------|---------------------------------|
| `<geohash>` | geohashを指定する必要があります。 |

## 戻り値の型

Geometry。

## SQL Examples

```sql
SELECT
  ST_GEOMPOINTFROMGEOHASH(
    's02equ0'
  ) AS pipeline_geometry;

┌──────────────────────────────────────────────┐
│               pipeline_geometry              │
│                   Geometry                   │
├──────────────────────────────────────────────┤
│ POINT(1.0004425048828125 2.0001983642578125) │
└──────────────────────────────────────────────┘
```
