---
title: ST_MAKEGEOMPOINT（Lakehouse v1）
description: ST_MAKEGEOMPOINT — 指定した経度と緯度のPointを表すGEOMETRYオブジェクトを作成します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-makegeompoint.md
---

指定した経度と緯度のPointを表すGEOMETRYオブジェクトを作成します。

## SQL Syntax

```sql
ST_MAKEGEOMPOINT(<longitude>, <latitude>)
```

## エイリアス

- [ST_GEOM_POINT](../st-geom-point)

## 引数

| 引数     | 説明                                   |
|---------------|-----------------------------------------------|
| `<longitude>` | 経度を表すDouble値。 |
| `<latitude>`  | 緯度を表すDouble値。  |

## 戻り値の型

Geometry。

## SQL Examples

```sql
SELECT
  ST_MAKEGEOMPOINT(
    7.0, 8.0
  ) AS pipeline_point;

┌────────────────┐
│ pipeline_point │
├────────────────┤
│ POINT(7 8)     │
└────────────────┘

SELECT
  ST_MAKEGEOMPOINT(
    -122.3061, 37.554162
  ) AS pipeline_point;

┌────────────────────────────┐
│       pipeline_point       │
├────────────────────────────┤
│ POINT(-122.3061 37.554162) │
└────────────────────────────┘
```
