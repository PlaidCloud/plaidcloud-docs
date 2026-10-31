---
title: ST_GEOMPOINTFROMGEOHASH（Lakehouse v1）
description: ST_GEOMPOINTFROMGEOHASH — 返回表示 geohash 中心点的 GEOMETRY 对象。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-geompointfromgeohash.md
---

返回表示 [geohash](https://en.wikipedia.org/wiki/Geohash) 中心点的 GEOMETRY 对象。

## SQL 语法

```sql
ST_GEOMPOINTFROMGEOHASH(<geohash>)
```

## 参数

| 参数        | 说明                     |
|-------------|--------------------------|
| `<geohash>` | 参数必须是 geohash。     |

## 返回类型

Geometry。

## SQL 示例

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
