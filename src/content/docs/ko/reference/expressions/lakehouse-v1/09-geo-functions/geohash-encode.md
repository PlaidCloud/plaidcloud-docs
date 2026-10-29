---
title: GEOHASH_ENCODE (Lakehouse v1)
description: GEOHASH_ENCODE — 위도와 경도 좌표 쌍을 Geohash로 인코딩된 문자열로 변환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/geohash-encode.md
---

위도와 경도 좌표 쌍을 [Geohash](https://en.wikipedia.org/wiki/Geohash)로 인코딩된 문자열로 변환합니다.

## Analyze 구문

```python
func.geohash_encode(lon, lat)
```

## Analyze 예제

```python
func.geohash_encode(-5.60302734375, 42.593994140625)

┌─────────────────────────────────────────────────────────┐
│ func.geohash_encode((- 5.60302734375), 42.593994140625) │
├─────────────────────────────────────────────────────────┤
│ ezs42d000000                                            │
└─────────────────────────────────────────────────────────┘
```

## SQL 구문

```sql
GEOHASH_ENCODE(lon, lat)
```

## SQL 예제

```sql
SELECT GEOHASH_ENCODE(-5.60302734375, 42.593994140625);

┌────────────────────────────────────────────────────┐
│ geohash_encode((- 5.60302734375), 42.593994140625) │
├────────────────────────────────────────────────────┤
│ ezs42d000000                                       │
└────────────────────────────────────────────────────┘
```
