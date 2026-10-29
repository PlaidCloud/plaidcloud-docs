---
title: HAVERSINE（Lakehouse v1）
description: HAVERSINE — 使用 Haversine 公式计算地球表面两点之间的大圆距离，单位为千米。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/haversine.md
---

使用 [Haversine 公式](https://en.wikipedia.org/wiki/Haversine_formula)计算地球表面两点之间的大圆距离，单位为千米。两点以度为单位的纬度和经度指定。

## SQL 语法

```sql
HAVERSINE(<lat1>, <lon1>, <lat2>, <lon2>)
```

## 参数

| 参数      | 说明                 |
|-----------|----------------------|
| `<lat1>`  | 第一个点的纬度。     |
| `<lon1>`  | 第一个点的经度。     |
| `<lat2>`  | 第二个点的纬度。     |
| `<lon2>`  | 第二个点的经度。     |

## 返回类型

Double。

## SQL 示例

```sql
SELECT
  HAVERSINE(40.7127, -74.0059, 34.0500, -118.2500) AS distance

┌────────────────┐
│    distance    │
├────────────────┤
│ 3936.390533556 │
└────────────────┘
```
