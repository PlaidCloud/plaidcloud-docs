---
title: ST_GEOMETRYFROMTEXT (Lakehouse v2)
description: ST_GEOMETRYFROMTEXT — WKT(Well-Known Text) 문자열로 지오메트리를 만듭니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/17-spatial-functions/st-geometryfromtext.md
---

WKT(Well-Known Text) 문자열로 지오메트리를 만듭니다.

## Analyze 구문

```python
func.st_geometryfromtext(<wkt>)
```

## Analyze 예제

```python
func.st_geometryfromtext('POINT (1 2)')

┌────────────┐
│ (geometry)  │
└────────────┘
```

## SQL 구문

```sql
ST_GEOMETRYFROMTEXT(<wkt>)
```

## SQL 예제

```sql
SELECT ST_ASTEXT(ST_GEOMETRYFROMTEXT('POINT (1 2)'));

┌─────────────┐
│ POINT (1 2)  │
└─────────────┘
```
