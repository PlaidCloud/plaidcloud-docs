---
title: ST_SRID（Lakehouse v1）
description: ST_SRID — GEOMETRYオブジェクトのSRID（空間参照系識別子）を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-srid.md
---

GEOMETRYオブジェクトのSRID（空間参照系識別子）を返します。

## SQL Syntax

```sql
ST_SRID(<geometry>)
```

## 引数

| 引数    | 説明                                          |
|--------------|------------------------------------------------------|
| `<geometry>` | GEOMETRY型の式を指定する必要があります。 |

## 戻り値の型

INT32。

:::note
GeometryにこのSRIDがない場合は、デフォルト値の4326が返されます。
:::

## SQL Examples

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
