---
title: ST_X（Lakehouse v1）
description: ST_X — GEOMETRYオブジェクトで表されるPointの経度（X座標）を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-x.md
---

GEOMETRYオブジェクトで表されるPointの経度（X座標）を返します。

## SQL Syntax

```sql
ST_X(<geometry>)
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
  ST_X(
    ST_MAKEGEOMPOINT(
      37.5, 45.5
    )
  ) AS pipeline_x;

┌────────────┐
│ pipeline_x │
├────────────┤
│       37.5 │
└────────────┘
```
