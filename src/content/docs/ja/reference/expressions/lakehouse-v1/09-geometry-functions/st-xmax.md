---
title: ST_XMAX（Lakehouse v1）
description: ST_XMAX — 指定したGEOMETRYオブジェクトに含まれるすべての点の最大経度（X座標）を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-xmax.md
---

指定したGEOMETRYオブジェクトに含まれるすべての点の最大経度（X座標）を返します。

## SQL Syntax

```sql
ST_XMAX(<geometry>)
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
  ST_XMAX(
    TO_GEOMETRY(
      'GEOMETRYCOLLECTION(POINT(40 10),LINESTRING(10 10,20 20,10 40),POINT EMPTY)'
    )
  ) AS pipeline_xmax;

┌───────────────┐
│ pipeline_xmax │
├───────────────┤
│            40 │
└───────────────┘

SELECT
  ST_XMAX(
    TO_GEOMETRY(
      'GEOMETRYCOLLECTION(POINT(40 10),LINESTRING(10 10,20 20,10 40),POLYGON((40 40,20 45,45 30,40 40)))'
    )
  ) AS pipeline_xmax;

┌───────────────┐
│ pipeline_xmax │
├───────────────┤
│            45 │
└───────────────┘
```
