---
title: ST_DISTANCE（Lakehouse v1）
description: ST_DISTANCE — 返回两个 GEOMETRY 对象之间的最小欧氏距离。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-distance.md
---

返回两个 GEOMETRY 对象之间的最小[欧氏距离](https://en.wikipedia.org/wiki/Euclidean_distance)。

## SQL 语法

```sql
ST_DISTANCE(<geometry1>, <geometry2>)
```

## 参数

| 参数          | 说明                                                  |
|---------------|-------------------------------------------------------|
| `<geometry1>` | 参数必须是 GEOMETRY 类型的表达式，且必须包含一个 Point。 |
| `<geometry2>` | 参数必须是 GEOMETRY 类型的表达式，且必须包含一个 Point。 |

:::note
- 如果一个或多个输入点为 NULL，则返回 NULL。
- 如果两个输入的 GEOMETRY 对象具有不同的 SRID，该函数会报错。
:::

## 返回类型

Double。

## SQL 示例

```sql
SELECT
  ST_DISTANCE(
    TO_GEOMETRY('POINT(0 0)'),
    TO_GEOMETRY('POINT(1 1)')
  ) AS distance

┌─────────────┐
│   distance  │
├─────────────┤
│ 1.414213562 │
└─────────────┘
```
