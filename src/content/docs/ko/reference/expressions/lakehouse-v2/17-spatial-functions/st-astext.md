---
title: ST_ASTEXT (Lakehouse v2)
description: ST_ASTEXT — 지오메트리를 WKT(Well-Known Text) 표현으로 변환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/17-spatial-functions/st-astext.md
---

지오메트리를 WKT(Well-Known Text) 표현으로 변환합니다.

## Analyze 구문

```python
func.st_astext(<geometry>)
```

## Analyze 예제

```python
func.st_astext(func.st_point(1, 2))

┌───────────────┐
│ 'POINT (1 2)'  │
└───────────────┘
```

## SQL 구문

```sql
ST_ASTEXT(<geometry>)
```

## SQL 예제

```sql
SELECT ST_ASTEXT(ST_POINT(1, 2));

┌─────────────┐
│ POINT (1 2)  │
└─────────────┘
```
