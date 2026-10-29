---
title: ST_SETSRID（Lakehouse v1）
description: ST_SETSRID — 返回其 SRID（空间参考系统标识符）已设置为指定值的 GEOMETRY 对象。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-setsrid.md
---

返回其 [SRID（空间参考系统标识符）](https://en.wikipedia.org/wiki/Spatial_reference_system#Identifier)已设置为指定值的 GEOMETRY 对象。此函数仅更改 SRID，不影响对象的坐标。如果还需要更改坐标以匹配新的 SRS（空间参考系统），请改用 [ST_TRANSFORM](../st-transform)。

## SQL 语法

```sql
ST_SETSRID(<geometry>, <srid>)
```

## 参数

| 参数         | 说明                                              |
|--------------|---------------------------------------------------|
| `<geometry>` | 参数必须是 GEOMETRY 对象类型的表达式。            |
| `<srid>`     | 要在返回的 GEOMETRY 对象中设置的 SRID 整数。      |

## 返回类型

Geometry。

## SQL 示例

```sql
SET GEOMETRY_OUTPUT_FORMAT = 'EWKT'

SELECT ST_SETSRID(TO_GEOMETRY('POINT(13 51)'), 4326) AS geometry

┌────────────────────────┐
│        geometry        │
├────────────────────────┤
│ SRID=4326;POINT(13 51) │
└────────────────────────┘

```
