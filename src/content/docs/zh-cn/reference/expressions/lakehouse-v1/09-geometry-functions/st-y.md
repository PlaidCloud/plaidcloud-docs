---
title: ST_Y（Lakehouse v1）
description: ST_Y — 返回 GEOMETRY 对象所表示的 Point 的纬度（Y 坐标）。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-y.md
---

返回 GEOMETRY 对象所表示的 Point 的纬度（Y 坐标）。

## SQL 语法

```sql
ST_Y(<geometry>)
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
