---
title: ST_LENGTH（Lakehouse v1）
description: ST_LENGTH — 返回 GEOMETRY 对象中 LineString 的欧氏长度。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-length.md
---

返回 GEOMETRY 对象中 LineString 的欧氏长度。

## SQL 语法

```sql
ST_LENGTH(<geometry>)
```

## 参数

| 参数         | 说明                                                        |
|--------------|-------------------------------------------------------------|
| `<geometry>` | 参数必须是包含线串的 GEOMETRY 类型表达式。                  |

:::note
- 如果 `<geometry>` 不是 `LineString`、`MultiLineString`，也不是包含线串的 `GeometryCollection`，则返回 0。
- 如果 `<geometry>` 是 `GeometryCollection`，则返回集合中各线串长度之和。
:::

## 返回类型

Double。

## SQL 示例

```sql
SELECT
  ST_LENGTH(TO_GEOMETRY('POINT(1 1)')) AS length

┌─────────┐
│  length │
├─────────┤
│       0 │
└─────────┘

SELECT
  ST_LENGTH(TO_GEOMETRY('LINESTRING(0 0, 1 1)')) AS length

┌─────────────┐
│    length   │
├─────────────┤
│ 1.414213562 │
└─────────────┘

SELECT
  ST_LENGTH(
    TO_GEOMETRY('POLYGON((0 0, 0 1, 1 1, 1 0, 0 0))')
  ) AS length

┌─────────┐
│  length │
├─────────┤
│       0 │
└─────────┘
```
