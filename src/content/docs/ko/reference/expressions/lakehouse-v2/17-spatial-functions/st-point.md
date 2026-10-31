---
title: ST_POINT (Lakehouse v2)
description: ST_POINT — 경도와 위도 값으로 포인트 지오메트리를 생성합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/17-spatial-functions/st-point.md
---

경도와 위도 값으로 포인트 지오메트리를 생성합니다.

## Analyze 구문

```python
func.st_point(<lng>, <lat>)
```

## Analyze 예제

```python
func.st_point(-73.9857, 40.7484)

┌────────────┐
│ (geometry)  │
└────────────┘
```

## SQL 구문

```sql
ST_POINT(<lng>, <lat>)
```

## SQL 예제

```sql
SELECT ST_ASTEXT(ST_POINT(-73.9857, 40.7484));

┌──────────────────────────┐
│ POINT (-73.9857 40.7484)  │
└──────────────────────────┘
```
