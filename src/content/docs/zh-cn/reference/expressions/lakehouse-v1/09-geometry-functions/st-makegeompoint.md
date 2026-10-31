---
title: ST_MAKEGEOMPOINT（Lakehouse v1）
description: ST_MAKEGEOMPOINT — 构造表示具有指定经纬度的 Point 的 GEOMETRY 对象。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-makegeompoint.md
---

构造表示具有指定经度和纬度的 Point 的 GEOMETRY 对象。

## SQL 语法

```sql
ST_MAKEGEOMPOINT(<longitude>, <latitude>)
```

## 别名

- [ST_GEOM_POINT](../st-geom-point)

## 参数

| 参数          | 说明                         |
|---------------|------------------------------|
| `<longitude>` | 表示经度的 Double 值。       |
| `<latitude>`  | 表示纬度的 Double 值。       |

## 返回类型

Geometry。

## SQL 示例

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
