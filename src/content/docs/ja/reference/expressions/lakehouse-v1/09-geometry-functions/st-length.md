---
title: ST_LENGTH（Lakehouse v1）
description: ST_LENGTH — GEOMETRYオブジェクト内のLineStringのユークリッド長を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-length.md
---

GEOMETRYオブジェクト内のLineStringのユークリッド長を返します。

## SQL Syntax

```sql
ST_LENGTH(<geometry>)
```

## 引数

| 引数    | 説明                                                                 |
|--------------|-----------------------------------------------------------------------------|
| `<geometry>` | linestringを含むGEOMETRY型の式を指定する必要があります。 |

:::note
- `<geometry>`が`LineString`、`MultiLineString`、またはlinestringを含む`GeometryCollection`のいずれでもない場合は、0を返します。
- `<geometry>`が`GeometryCollection`の場合は、コレクション内のlinestringの長さの合計を返します。
:::

## 戻り値の型

Double。

## SQL Examples

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
