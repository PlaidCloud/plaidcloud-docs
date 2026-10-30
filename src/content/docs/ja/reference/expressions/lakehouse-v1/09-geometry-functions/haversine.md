---
title: HAVERSINE（Lakehouse v1）
description: HAVERSINE — ハーヴァサイン公式を使用して、地球表面上の2点間の大円距離をキロメートルで計算します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/haversine.md
---

[ハーヴァサイン公式](https://en.wikipedia.org/wiki/Haversine_formula)を使用して、地球表面上の2点間の大円距離をキロメートルで計算します。2点は、度単位の緯度と経度で指定します。

## SQL Syntax

```sql
HAVERSINE(<lat1>, <lon1>, <lat2>, <lon2>)
```

## 引数

| 引数 | 説明                        |
|-----------|------------------------------------|
| `<lat1>`  | 1つ目の点の緯度。   |
| `<lon1>`  | 1つ目の点の経度。  |
| `<lat2>`  | 2つ目の点の緯度。  |
| `<lon2>`  | 2つ目の点の経度。 |

## 戻り値の型

Double。

## SQL Examples

```sql
SELECT
  HAVERSINE(40.7127, -74.0059, 34.0500, -118.2500) AS distance

┌────────────────┐
│    distance    │
├────────────────┤
│ 3936.390533556 │
└────────────────┘
```
