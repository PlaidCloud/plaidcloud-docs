---
title: ST_ENDPOINT（Lakehouse v1）
description: ST_ENDPOINT — 返回 LineString 中的最后一个 Point。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-endpoint.md
---

返回 LineString 中的最后一个 Point。

## SQL 语法

```sql
ST_ENDPOINT(<geometry>)
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
  ST_ENDPOINT(
    ST_GEOMETRYFROMWKT(
      'LINESTRING(1 1, 2 2, 3 3, 4 4)'
    )
  ) AS pipeline_endpoint;

┌───────────────────┐
│ pipeline_endpoint │
├───────────────────┤
│ POINT(4 4)        │
└───────────────────┘
```
