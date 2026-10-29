---
title: GEOHASH_DECODE（Lakehouse v1）
description: GEOHASH_DECODE — Geohashでエンコードされた文字列を緯度・経度の座標に変換します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/geohash-decode.md
---

[Geohash](https://en.wikipedia.org/wiki/Geohash)でエンコードされた文字列を緯度・経度の座標に変換します。

## Analyze Syntax

```python
func.geohash_decode('<geohashed-string\>')
```

## Analyze Examples

```python
func.geohash_decode('ezs42')

┌─────────────────────────────────┐
│  func.geohash_decode('ezs42')   │
├─────────────────────────────────┤
│ (-5.60302734375,42.60498046875) │
└─────────────────────────────────┘
```

## SQL Syntax

```sql
GEOHASH_DECODE('<geohashed-string\>')
```

## SQL Examples

```sql
SELECT GEOHASH_DECODE('ezs42');

┌─────────────────────────────────┐
│     geohash_decode('ezs42')     │
├─────────────────────────────────┤
│ (-5.60302734375,42.60498046875) │
└─────────────────────────────────┘
```
