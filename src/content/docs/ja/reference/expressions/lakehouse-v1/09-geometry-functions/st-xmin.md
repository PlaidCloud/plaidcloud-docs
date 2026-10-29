---
title: ST_XMIN（Lakehouse v1）
description: ST_XMIN — 指定したGEOMETRYオブジェクトに含まれるすべての点の最小経度（X座標）を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-xmin.md
---

指定したGEOMETRYオブジェクトに含まれるすべての点の最小経度（X座標）を返します。

## SQL Syntax

```sql
ST_XMIN(<geometry>)
```

## 引数

| 引数    | 説明                                          |
|--------------|------------------------------------------------------|
| `<geometry>` | GEOMETRY型の式を指定する必要があります。 |

## 戻り値の型

Double。

## SQL Examples

```sql
SELECT
  ST_XMIN(
    TO_GEOMETRY(
      'GEOMETRYCOLLECTION(POINT(180 10),LINESTRING(20 10,30 20,40 40),POINT EMPTY)'
    )
  ) AS pipeline_xmin;

┌───────────────┐
│ pipeline_xmin │
├───────────────┤
│            20 │
└───────────────┘

SELECT
  ST_XMIN(
    TO_GEOMETRY(
      'GEOMETRYCOLLECTION(POINT(40 10),LINESTRING(20 10,30 20,10 40),POLYGON((40 40,20 45,45 30,40 40)))'
    )
  ) AS pipeline_xmin;

┌───────────────┐
│ pipeline_xmin │
├───────────────┤
│            10 │
└───────────────┘
```
