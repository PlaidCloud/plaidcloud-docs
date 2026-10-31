---
title: HAVERSINE (Lakehouse v1)
description: HAVERSINE — 하버사인 공식을 사용하여 지표면 위 두 지점 사이의 대원 거리를 킬로미터 단위로 계산합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/haversine.md
---

[하버사인 공식](https://en.wikipedia.org/wiki/Haversine_formula)을 사용하여 지표면 위 두 지점 사이의 대원 거리를 킬로미터 단위로 계산합니다. 두 지점은 도 단위의 위도와 경도로 지정합니다.

## SQL 구문

```sql
HAVERSINE(<lat1>, <lon1>, <lat2>, <lon2>)
```

## 인수

| 인수 | 설명                        |
|-----------|------------------------------------|
| `<lat1>`  | 첫 번째 지점의 위도입니다.   |
| `<lon1>`  | 첫 번째 지점의 경도입니다.  |
| `<lat2>`  | 두 번째 지점의 위도입니다.  |
| `<lon2>`  | 두 번째 지점의 경도입니다. |

## 반환 형식

Double.

## SQL 예제

```sql
SELECT
  HAVERSINE(40.7127, -74.0059, 34.0500, -118.2500) AS distance

┌────────────────┐
│    distance    │
├────────────────┤
│ 3936.390533556 │
└────────────────┘
```
