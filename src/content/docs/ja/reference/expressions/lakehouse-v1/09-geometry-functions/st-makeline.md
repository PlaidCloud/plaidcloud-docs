---
title: ST_MAKELINE（Lakehouse v1）
description: ST_MAKELINE — 入力された2つのGEOMETRYオブジェクトの点を結ぶ線を表すGEOMETRYオブジェクトを作成します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-makeline.md
---

入力された2つのGEOMETRYオブジェクトの点を結ぶ線を表すGEOMETRYオブジェクトを作成します。

## SQL Syntax

```sql
ST_MAKELINE(<geometry1>, <geometry2>)
```

## エイリアス

- [ST_MAKE_LINE](../st-make-line)

## 引数

| 引数     | 説明                                                                                                 |
|---------------|-------------------------------------------------------------------------------------------------------------|
| `<geometry1>` | 結ぶ点を含むGEOMETRYオブジェクト。このオブジェクトは、Point、MultiPoint、またはLineStringである必要があります。 |
| `<geometry2>` | 結ぶ点を含むGEOMETRYオブジェクト。このオブジェクトは、Point、MultiPoint、またはLineStringである必要があります。 |

## 戻り値の型

Geometry。

## SQL Examples

```sql
SELECT
  ST_MAKELINE(
    ST_GEOMETRYFROMWKT(
      'POINT(-122.306100 37.554162)'
    ),
    ST_GEOMETRYFROMWKT(
      'POINT(-104.874173 56.714538)'
    )
  ) AS pipeline_line;

┌───────────────────────────────────────────────────────┐
│                     pipeline_line                     │
├───────────────────────────────────────────────────────┤
│ LINESTRING(-122.3061 37.554162,-104.874173 56.714538) │
└───────────────────────────────────────────────────────┘
```
