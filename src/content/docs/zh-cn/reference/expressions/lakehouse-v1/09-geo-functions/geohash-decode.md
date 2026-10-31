---
title: GEOHASH_DECODE（Lakehouse v1）
description: GEOHASH_DECODE — 将 Geohash 编码的字符串转换为经纬度坐标。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/geohash-decode.md
---

将 [Geohash](https://en.wikipedia.org/wiki/Geohash) 编码的字符串转换为经纬度坐标。

## Analyze 语法

```python
func.geohash_decode('<geohashed-string\>')
```

## Analyze 示例

```python
func.geohash_decode('ezs42')

┌─────────────────────────────────┐
│  func.geohash_decode('ezs42')   │
├─────────────────────────────────┤
│ (-5.60302734375,42.60498046875) │
└─────────────────────────────────┘
```

## SQL 语法

```sql
GEOHASH_DECODE('<geohashed-string\>')
```

## SQL 示例

```sql
SELECT GEOHASH_DECODE('ezs42');

┌─────────────────────────────────┐
│     geohash_decode('ezs42')     │
├─────────────────────────────────┤
│ (-5.60302734375,42.60498046875) │
└─────────────────────────────────┘
```
