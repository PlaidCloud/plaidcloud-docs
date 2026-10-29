---
title: ST_CIRCLE (Lakehouse v2)
description: ST_CIRCLE — 중심의 경도, 위도와 반지름(미터)으로 원 지오메트리를 만듭니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/17-spatial-functions/st-circle.md
---

중심의 경도, 위도와 반지름(미터)으로 원 지오메트리를 만듭니다.

## Analyze 구문

```python
func.st_circle(<lng>, <lat>, <radius>)
```

## Analyze 예제

```python
func.st_circle(0, 0, 100)

┌────────────┐
│ (geometry)  │
└────────────┘
```

## SQL 구문

```sql
ST_CIRCLE(<lng>, <lat>, <radius>)
```

## SQL 예제

```sql
SELECT ST_ASTEXT(ST_CIRCLE(0, 0, 100));

┌─────────────────────┐
│ CIRCLE((0, 0), 100)  │
└─────────────────────┘
```
