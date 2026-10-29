---
title: ST_MAKELINE（Lakehouse v1）
description: ST_MAKELINE — 构造表示连接两个输入 GEOMETRY 对象中各点的线的 GEOMETRY 对象。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-makeline.md
---

构造表示连接两个输入 GEOMETRY 对象中各点的线的 GEOMETRY 对象。

## SQL 语法

```sql
ST_MAKELINE(<geometry1>, <geometry2>)
```

## 别名

- [ST_MAKE_LINE](../st-make-line)

## 参数

| 参数          | 说明                                                                          |
|---------------|-------------------------------------------------------------------------------|
| `<geometry1>` | 包含要连接的点的 GEOMETRY 对象。该对象必须是 Point、MultiPoint 或 LineString。 |
| `<geometry2>` | 包含要连接的点的 GEOMETRY 对象。该对象必须是 Point、MultiPoint 或 LineString。 |

## 返回类型

Geometry。

## SQL 示例

```sql
SELECT
  ST_MAKELINE(
    ST_GEOMETRYFROMWKT(
      'POINT(-122.306100 37.554162)'
    ),
    ST_GEOMETRYFROMWKT(
      'POINT(-104.874173 56.714538)'
    )
  ) AS pipeline_line;

┌───────────────────────────────────────────────────────┐
│                     pipeline_line                     │
├───────────────────────────────────────────────────────┤
│ LINESTRING(-122.3061 37.554162,-104.874173 56.714538) │
└───────────────────────────────────────────────────────┘
```
