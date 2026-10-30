---
title: ST_ASWKB（Lakehouse v1）
description: ST_ASWKB — 将 GEOMETRY 对象转换为 WKB（众所周知的二进制）格式表示。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-aswkb.md
---

将 GEOMETRY 对象转换为 [WKB（众所周知的二进制）](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry#Well-known_binary)格式表示。

## SQL 语法

```sql
ST_ASWKB(<geometry>)
```

## 别名

- [ST_ASBINARY](../st-asbinary)

## 参数

| 参数         | 说明                                   |
|--------------|----------------------------------------|
| `<geometry>` | 参数必须是 GEOMETRY 类型的表达式。     |

## 返回类型

Binary。

## SQL 示例

```sql
SELECT
  ST_ASWKB(
    ST_GEOMETRYFROMWKT(
      'SRID=4326;LINESTRING(400000 6000000, 401000 6010000)'
    )
  ) AS pipeline_wkb;

┌────────────────────────────────────────────────────────────────────────────────────┐
│                                    pipeline_wkb                                    │
├────────────────────────────────────────────────────────────────────────────────────┤
│ 01020000000200000000000000006A18410000000060E3564100000000A07918410000000024ED5641 │
└────────────────────────────────────────────────────────────────────────────────────┘

SELECT
  ST_ASBINARY(
    ST_GEOMETRYFROMWKT(
      'SRID=4326;POINT(-122.35 37.55)'
    )
  ) AS pipeline_wkb;

┌────────────────────────────────────────────┐
│                pipeline_wkb                │
├────────────────────────────────────────────┤
│ 01010000006666666666965EC06666666666C64240 │
└────────────────────────────────────────────┘
```
