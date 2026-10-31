---
title: ST_POLYGON (Lakehouse v2)
description: ST_POLYGON — WKT 문자열로 폴리곤 지오메트리를 생성합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/17-spatial-functions/st-polygon.md
---

WKT 문자열로 폴리곤 지오메트리를 생성합니다.

## Analyze 구문

```python
func.st_polygon(<wkt>)
```

## Analyze 예제

```python
func.st_polygon('POLYGON((0 0,10 0,10 10,0 10,0 0))')

┌────────────┐
│ (geometry)  │
└────────────┘
```

## SQL 구문

```sql
ST_POLYGON(<wkt>)
```

## SQL 예제

```sql
SELECT ST_ASTEXT(ST_POLYGON('POLYGON((0 0,10 0,10 10,0 10,0 0))'));

┌─────────────────────────────────────────┐
│ POLYGON ((0 0, 10 0, 10 10, 0 10, 0 0))  │
└─────────────────────────────────────────┘
```
