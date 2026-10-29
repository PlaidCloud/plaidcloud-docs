---
title: ST_X（Lakehouse v1）
description: ST_X — 返回 GEOMETRY 对象所表示的 Point 的经度（X 坐标）。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-x.md
---

返回 GEOMETRY 对象所表示的 Point 的经度（X 坐标）。

## SQL 语法

```sql
ST_X(<geometry>)
```

## 参数

| 参数         | 说明                                                    |
|--------------|---------------------------------------------------------|
| `<geometry>` | 参数必须是 GEOMETRY 类型的表达式，且必须包含一个 Point。 |

## 返回类型

Double。

## SQL 示例

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
