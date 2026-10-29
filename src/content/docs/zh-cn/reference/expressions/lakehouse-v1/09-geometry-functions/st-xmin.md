---
title: ST_XMIN（Lakehouse v1）
description: ST_XMIN — 返回指定 GEOMETRY 对象所含全部点的最小经度（X 坐标）。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-xmin.md
---

返回指定 GEOMETRY 对象所含全部点的最小经度（X 坐标）。

## SQL 语法

```sql
ST_XMIN(<geometry>)
```

## 参数

| 参数         | 说明                                   |
|--------------|----------------------------------------|
| `<geometry>` | 参数必须是 GEOMETRY 类型的表达式。     |

## 返回类型

Double。

## SQL 示例

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
