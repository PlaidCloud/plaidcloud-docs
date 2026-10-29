---
title: GEOHASH_DECODE (Lakehouse v1)
description: GEOHASH_DECODE — Geohash로 인코딩된 문자열을 위도/경도 좌표로 변환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/geohash-decode.md
---

[Geohash](https://en.wikipedia.org/wiki/Geohash)로 인코딩된 문자열을 위도/경도 좌표로 변환합니다.

## Analyze 구문

```python
func.geohash_decode('<geohashed-string\>')
```

## Analyze 예제

```python
func.geohash_decode('ezs42')

┌─────────────────────────────────┐
│  func.geohash_decode('ezs42')   │
├─────────────────────────────────┤
│ (-5.60302734375,42.60498046875) │
└─────────────────────────────────┘
```

## SQL 구문

```sql
GEOHASH_DECODE('<geohashed-string\>')
```

## SQL 예제

```sql
SELECT GEOHASH_DECODE('ezs42');

┌─────────────────────────────────┐
│     geohash_decode('ezs42')     │
├─────────────────────────────────┤
│ (-5.60302734375,42.60498046875) │
└─────────────────────────────────┘
```
