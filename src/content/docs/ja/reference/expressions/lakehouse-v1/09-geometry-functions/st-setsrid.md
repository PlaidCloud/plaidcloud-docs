---
title: ST_SETSRID（Lakehouse v1）
description: ST_SETSRID — SRID（空間参照系識別子）を設定したGEOMETRYオブジェクトを返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-setsrid.md
---

[SRID（空間参照系識別子）](https://en.wikipedia.org/wiki/Spatial_reference_system#Identifier)を指定した値に設定したGEOMETRYオブジェクトを返します。この関数はSRIDのみを変更し、オブジェクトの座標には影響しません。新しいSRS（空間参照系）に合わせて座標も変更する必要がある場合は、代わりに[ST_TRANSFORM](../st-transform)を使用してください。

## SQL Syntax

```sql
ST_SETSRID(<geometry>, <srid>)
```

## 引数

| 引数    | 説明                                                 |
|--------------|-------------------------------------------------------------|
| `<geometry>` | GEOMETRYオブジェクト型の式を指定する必要があります。 |
| `<srid>`     | 返されるGEOMETRYオブジェクトに設定するSRIDの整数値。    |

## 戻り値の型

Geometry。

## SQL Examples

```sql
SET GEOMETRY_OUTPUT_FORMAT = 'EWKT'

SELECT ST_SETSRID(TO_GEOMETRY('POINT(13 51)'), 4326) AS geometry

┌────────────────────────┐
│        geometry        │
├────────────────────────┤
│ SRID=4326;POINT(13 51) │
└────────────────────────┘

```
