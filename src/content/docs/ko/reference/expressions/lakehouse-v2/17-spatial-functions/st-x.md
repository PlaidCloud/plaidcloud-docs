---
title: ST_X (Lakehouse v2)
description: ST_X — 포인트 지오메트리의 X 좌표(경도)를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/17-spatial-functions/st-x.md
---

포인트 지오메트리의 X 좌표(경도)를 반환합니다.

## Analyze 구문

```python
func.st_x(<point>)
```

## Analyze 예제

```python
func.st_x(func.st_point(1.5, 2.5))

┌─────┐
│ 1.5  │
└─────┘
```

## SQL 구문

```sql
ST_X(<point>)
```

## SQL 예제

```sql
SELECT ST_X(ST_POINT(1.5, 2.5));

┌─────┐
│ 1.5  │
└─────┘
```
