---
title: ST_CONTAINS（Lakehouse v1）
description: ST_CONTAINS — 2つ目のGEOMETRYオブジェクトが1つ目の完全に内側にある場合にTRUEを返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-contains.md
---

2つ目のGEOMETRYオブジェクトが1つ目のGEOMETRYオブジェクトの完全に内側にある場合にTRUEを返します。

## SQL Syntax

```sql
ST_CONTAINS(<geometry1>, <geometry2>)
```

## 引数

| 引数     | 説明                                                                                  |
|---------------|----------------------------------------------------------------------------------------------|
| `<geometry1>` | GeometryCollectionではないGEOMETRYオブジェクト型の式を指定する必要があります。 |
| `<geometry2>` | GeometryCollectionではないGEOMETRYオブジェクト型の式を指定する必要があります。 |

:::note
- 2つの入力GEOMETRYオブジェクトのSRIDが異なる場合、この関数はエラーを報告します。
:::

## 戻り値の型

Boolean。

## SQL Examples

```sql
SELECT ST_CONTAINS(TO_GEOMETRY('POLYGON((-2 0, 0 2, 2 0, -2 0))'), TO_GEOMETRY('POLYGON((-1 0, 0 1, 1 0, -1 0))')) AS contains

┌──────────┐
│ contains │
├──────────┤
│ true     │
└──────────┘

SELECT ST_CONTAINS(TO_GEOMETRY('POLYGON((-2 0, 0 2, 2 0, -2 0))'), TO_GEOMETRY('LINESTRING(-1 1, 0 2, 1 1)')) AS contains

┌──────────┐
│ contains │
├──────────┤
│ false    │
└──────────┘

SELECT ST_CONTAINS(TO_GEOMETRY('POLYGON((-2 0, 0 2, 2 0, -2 0))'), TO_GEOMETRY('LINESTRING(-2 0, 0 0, 0 1)')) AS contains

┌──────────┐
│ contains │
├──────────┤
│ true     │
└──────────┘

```
