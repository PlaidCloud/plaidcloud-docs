---
title: ST_STARTPOINT（Lakehouse v1）
description: ST_STARTPOINT — LineStringの最初のPointを返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-startpoint.md
---

LineStringの最初のPointを返します。

## SQL Syntax

```sql
ST_STARTPOINT(<geometry>)
```

## 引数

| 引数    | 説明                                                                       |
|--------------|-----------------------------------------------------------------------------------|
| `<geometry>` | LineStringを表すGEOMETRY型の式を指定する必要があります。 |

## 戻り値の型

Geometry。

## SQL Examples

```sql
SELECT
  ST_STARTPOINT(
    ST_GEOMETRYFROMWKT(
      'LINESTRING(1 1, 2 2, 3 3, 4 4)'
    )
  ) AS pipeline_endpoint;

┌───────────────────┐
│ pipeline_endpoint │
├───────────────────┤
│ POINT(1 1)        │
└───────────────────┘
```
