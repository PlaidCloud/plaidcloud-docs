---
title: ST_ENDPOINT（Lakehouse v1）
description: ST_ENDPOINT — LineStringの最後のPointを返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-endpoint.md
---

LineStringの最後のPointを返します。

## SQL Syntax

```sql
ST_ENDPOINT(<geometry>)
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
  ST_ENDPOINT(
    ST_GEOMETRYFROMWKT(
      'LINESTRING(1 1, 2 2, 3 3, 4 4)'
    )
  ) AS pipeline_endpoint;

┌───────────────────┐
│ pipeline_endpoint │
├───────────────────┤
│ POINT(4 4)        │
└───────────────────┘
```
