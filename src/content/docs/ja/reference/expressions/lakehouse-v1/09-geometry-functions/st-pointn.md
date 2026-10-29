---
title: ST_POINTN（Lakehouse v1）
description: ST_POINTN — LineString内の指定したインデックスのPointを返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-pointn.md
---

LineString内の指定したインデックスのPointを返します。

## SQL Syntax

```sql
ST_POINTN(<geometry>, <index>)
```

## 引数

| 引数    | 説明                                                                       |
|--------------|-----------------------------------------------------------------------------------|
| `<geometry>` | LineStringを表すGEOMETRY型の式を指定する必要があります。 |
| `<index>`    | 返すPointのインデックス。                                                 |

:::note
インデックスは1から始まります。負のインデックスは、LineStringの末尾からのオフセットとして扱われます。インデックスが範囲外の場合、この関数はエラーを返します。
:::

## 戻り値の型

Geometry。

## SQL Examples

```sql
SELECT
  ST_POINTN(
    ST_GEOMETRYFROMWKT(
      'LINESTRING(1 1, 2 2, 3 3, 4 4)'
    ),
    1
  ) AS pipeline_pointn;

┌─────────────────┐
│ pipeline_pointn │
├─────────────────┤
│ POINT(1 1)      │
└─────────────────┘

SELECT
  ST_POINTN(
    ST_GEOMETRYFROMWKT(
      'LINESTRING(1 1, 2 2, 3 3, 4 4)'
    ),
    -2
  ) AS pipeline_pointn;

┌─────────────────┐
│ pipeline_pointn │
├─────────────────┤
│ POINT(3 3)      │
└─────────────────┘
```
