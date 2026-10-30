---
title: GEOHASH_ENCODE（Lakehouse v1）
description: GEOHASH_ENCODE — 将一对经纬度坐标转换为 Geohash 编码的字符串。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/geohash-encode.md
---

将一对经纬度坐标转换为 [Geohash](https://en.wikipedia.org/wiki/Geohash) 编码的字符串。

## Analyze 语法

```python
func.geohash_encode(lon, lat)
```

## Analyze 示例

```python
func.geohash_encode(-5.60302734375, 42.593994140625)

┌─────────────────────────────────────────────────────────┐
│ func.geohash_encode((- 5.60302734375), 42.593994140625) │
├─────────────────────────────────────────────────────────┤
│ ezs42d000000                                            │
└─────────────────────────────────────────────────────────┘
```

## SQL 语法

```sql
GEOHASH_ENCODE(lon, lat)
```

## SQL 示例

```sql
SELECT GEOHASH_ENCODE(-5.60302734375, 42.593994140625);

┌────────────────────────────────────────────────────┐
│ geohash_encode((- 5.60302734375), 42.593994140625) │
├────────────────────────────────────────────────────┤
│ ezs42d000000                                       │
└────────────────────────────────────────────────────┘
```
