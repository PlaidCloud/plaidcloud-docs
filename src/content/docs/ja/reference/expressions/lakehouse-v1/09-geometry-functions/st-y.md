---
title: ST_Y（Lakehouse v1）
description: ST_Y — GEOMETRYオブジェクトで表されるPointの緯度（Y座標）を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-y.md
---

GEOMETRYオブジェクトで表されるPointの緯度（Y座標）を返します。

## SQL Syntax

```sql
ST_Y(<geometry>)
```

## 引数

| 引数    | 説明                                                                   |
|--------------|-------------------------------------------------------------------------------|
| `<geometry>` | GEOMETRY型の式で、Pointを含んでいる必要があります。 |

## 戻り値の型

Double。

## SQL Examples

```sql
SELECT
  ST_Y(
    ST_MAKEGEOMPOINT(
      37.5, 45.5
    )
  ) AS pipeline_y;

┌────────────┐
│ pipeline_y │
├────────────┤
│       45.5 │
└────────────┘
```
