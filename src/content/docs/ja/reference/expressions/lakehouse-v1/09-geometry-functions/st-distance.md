---
title: ST_DISTANCE（Lakehouse v1）
description: ST_DISTANCE — 2つのGEOMETRYオブジェクト間の最小ユークリッド距離を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-distance.md
---

2つのGEOMETRYオブジェクト間の最小の[ユークリッド距離](https://en.wikipedia.org/wiki/Euclidean_distance)を返します。

## SQL Syntax

```sql
ST_DISTANCE(<geometry1>, <geometry2>)
```

## 引数

| 引数     | 説明                                                                   |
|---------------|-------------------------------------------------------------------------------|
| `<geometry1>` | GEOMETRY型の式で、Pointを含んでいる必要があります。 |
| `<geometry2>` | GEOMETRY型の式で、Pointを含んでいる必要があります。 |

:::note
- 入力の点の1つ以上がNULLの場合は、NULLを返します。
- 2つの入力GEOMETRYオブジェクトのSRIDが異なる場合、この関数はエラーを報告します。
:::

## 戻り値の型

Double。

## SQL Examples

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
