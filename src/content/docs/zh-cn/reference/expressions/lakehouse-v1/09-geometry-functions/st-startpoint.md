---
title: ST_STARTPOINT（Lakehouse v1）
description: ST_STARTPOINT — 返回 LineString 中的第一个 Point。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-startpoint.md
---

返回 LineString 中的第一个 Point。

## SQL 语法

```sql
ST_STARTPOINT(<geometry>)
```

## 参数

| 参数         | 说明                                                    |
|--------------|---------------------------------------------------------|
| `<geometry>` | 参数必须是表示 LineString 的 GEOMETRY 类型表达式。      |

## 返回类型

Geometry。

## SQL 示例

```sql
SELECT
  ST_STARTPOINT(
    ST_GEOMETRYFROMWKT(
      'LINESTRING(1 1, 2 2, 3 3, 4 4)'
    )
  ) AS pipeline_endpoint;

┌───────────────────┐
│ pipeline_endpoint │
├───────────────────┤
│ POINT(1 1)        │
└───────────────────┘
```
