---
title: ST_Y (Lakehouse v2)
description: ST_Y — 포인트 지오메트리의 Y 좌표(위도)를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/17-spatial-functions/st-y.md
---

포인트 지오메트리의 Y 좌표(위도)를 반환합니다.

## Analyze 구문

```python
func.st_y(<point>)
```

## Analyze 예제

```python
func.st_y(func.st_point(1.5, 2.5))

┌─────┐
│ 2.5  │
└─────┘
```

## SQL 구문

```sql
ST_Y(<point>)
```

## SQL 예제

```sql
SELECT ST_Y(ST_POINT(1.5, 2.5));

┌─────┐
│ 2.5  │
└─────┘
```
