---
title: GEOHASH_ENCODE（Lakehouse v1）
description: GEOHASH_ENCODE — 緯度と経度の座標のペアをGeohash形式の文字列に変換します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/geohash-encode.md
---

緯度と経度の座標のペアを[Geohash](https://en.wikipedia.org/wiki/Geohash)でエンコードされた文字列に変換します。

## Analyze Syntax

```python
func.geohash_encode(lon, lat)
```

## Analyze Examples

```python
func.geohash_encode(-5.60302734375, 42.593994140625)

┌─────────────────────────────────────────────────────────┐
│ func.geohash_encode((- 5.60302734375), 42.593994140625) │
├─────────────────────────────────────────────────────────┤
│ ezs42d000000                                            │
└─────────────────────────────────────────────────────────┘
```

## SQL Syntax

```sql
GEOHASH_ENCODE(lon, lat)
```

## SQL Examples

```sql
SELECT GEOHASH_ENCODE(-5.60302734375, 42.593994140625);

┌────────────────────────────────────────────────────┐
│ geohash_encode((- 5.60302734375), 42.593994140625) │
├────────────────────────────────────────────────────┤
│ ezs42d000000                                       │
└────────────────────────────────────────────────────┘
```
