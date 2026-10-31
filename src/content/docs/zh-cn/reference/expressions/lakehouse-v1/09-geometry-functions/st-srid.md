---
title: ST_SRID（Lakehouse v1）
description: ST_SRID — 返回 GEOMETRY 对象的 SRID（空间参考系统标识符）。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-srid.md
---

返回 GEOMETRY 对象的 SRID（空间参考系统标识符）。

## SQL 语法

```sql
ST_SRID(<geometry>)
```

## 参数

| 参数         | 说明                                   |
|--------------|----------------------------------------|
| `<geometry>` | 参数必须是 GEOMETRY 类型的表达式。     |

## 返回类型

INT32。

:::note
如果 Geometry 没有 SRID，则返回默认值 4326。
:::

## SQL 示例

```sql
SELECT
  ST_SRID(
    TO_GEOMETRY(
      'POINT(-122.306100 37.554162)',
      1234
    )
  ) AS pipeline_srid;

┌───────────────┐
│ pipeline_srid │
├───────────────┤
│          1234 │
└───────────────┘

SELECT
  ST_SRID(
    ST_MAKEGEOMPOINT(
      37.5, 45.5
    )
  ) AS pipeline_srid;

┌───────────────┐
│ pipeline_srid │
├───────────────┤
│          4326 │
└───────────────┘
```
